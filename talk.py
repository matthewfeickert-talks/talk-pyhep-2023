# %% [markdown]
# # [PyHEP 2023: `pyhf` upcoming features and development](https://indico.cern.ch/event/1252095/contributions/5592418/)

# %%
import pyhf
import cabinetry

# %%
pyhf.set_backend("jax")

# %% [markdown]
# ## `pyhf` `v0.8.0rc1` (coming soon)

# %% [markdown]
# Aim was to have a release candidate up for PyHEP 2023, but didn't hit quite hit that.

# %% [markdown]
# ### Custom modifiers

# %% [markdown]
# [Highly requested feature](https://github.com/scikit-hep/pyhf/issues/850) to be able to extend the modifiers with custom functions, provided through a new `experimental` extra
#
# ```
# python -m pip install --upgrade 'pyhf[experimental]'  # not yet, but once pyhf v0.8.0rc1 is out
# ```

# %%
import pyhf.experimental.modifiers

# %%
new_params = {
    "m1": {"inits": (1.0,), "bounds": ((-5.0, 5.0),)},
    "m2": {"inits": (1.0,), "bounds": ((-5.0, 5.0),)},
}

expanded_pyhf = pyhf.experimental.modifiers.add_custom_modifier(
    "custom", ["m1", "m2"], new_params
)

# %%
model = pyhf.Model(
    {
        "channels": [
            {
                "name": "singlechannel",
                "samples": [
                    {
                        "name": "signal",
                        "data": [10, 20],
                        "modifiers": [
                            {
                                "name": "f2",
                                "type": "custom",
                                "data": {"expr": "m1"},
                            },
                        ],
                    },
                    {
                        "name": "background",
                        "data": [100, 150],
                        "modifiers": [
                            {
                                "name": "f1",
                                "type": "custom",
                                "data": {"expr": "m1+(m2**2)"},
                            },
                        ],
                    },
                ],
            }
        ]
    },
    modifier_set=expanded_pyhf,
    poi_name="m1",
    validate=False,
    batch_size=1,
)

# %%
model.config.modifiers

# %%
model.expected_actualdata([[1.0, 2.0]])

# %% [markdown]
# ## Ecosystem extensions

# %% [markdown]
# ✨ **Checkout [Malin Horstmann's talk on Wednesday on Bayesian and frequentist methodologies with `pyhf`](https://indico.cern.ch/event/1252095/timetable/#19-bayesian-and-frequentist-me)**

# %% [markdown]
# Not going to go into the API today as there's a great talk on it later in the workshop

# %%
import Bayesian_pyhf

# %%
import Bayesian_pyhf.infer

# %%
# ? Bayesian_pyhf.infer.model

# %% [markdown]
# <br>
#
# Beginnging to explore the [concept of a plugin system for `pyhf`](https://github.com/scikit-hep/pyhf/issues/2233) to make it easier for tools to build on top.
#
# The goal would be that instead of having to do both
#
# ```python
# import pyhf
# import Bayesian_pyhf
# ```
#
# that in the future you would just do
#
# ```
# python -m pip install --upgrade pyhf bayesian-pyhf  # not yet on PyPI
# ```
#
# and then the following
#
# ```python
# import pyhf
# pyhf.bayes  # this isn't a real API, just an example of an idea
# ```
#
# would work without additional imports.

# %% [markdown]
# ### Plugin system for backends

# %% [markdown]
# Recent advances in the [Python array API standard](https://data-apis.org/array-api/) have lead to the Array API compatibility library [`array-api-compat`](https://github.com/data-apis/array-api-compat), which allows interoperability to any Array library that impliments the standard. 
#
# * Currently supported: NumPy, CuPy, PyTorch
# * Implimenting: JAX

# %%
import array_api_compat


# %% [markdown]
# Impliment once with `array-api-compat`

# %%
def example_function(x, y):
    xp = array_api_compat.array_namespace(x, y)
    # Now use xp as the array library namespace
    return xp.mean(x, axis=0) + 2 * xp.std(y, axis=0)


# %% [markdown]
# and then execute the same function code with NumPy

# %%
import numpy as np

np_x = np.arange(0., 100.)
np_y = np.square(np_x)

example_function(np_x, np_y)

# %% [markdown]
# as well as PyTorch

# %%
import torch

torch_x = torch.arange(0., 100.)
torch_y = torch.square(torch_x)

example_function(torch_x, torch_y)

# %% [markdown]
# Don't have access to GPUs for today's demo, but if we did CuPy would work as well

# %% [markdown]
# ```
# # micromamba install --channel conda-forge cupy
# ```
#
# ```python
# import cupy as cp
#
# cp_x = cp.arange(0., 100.)
# cp_y = cp.square(cp_x)
#
# example_function(cp_x, cp_y)  # array(5956.09328209)
# ```

# %% [markdown]
# While `pyhf` already has the `pyhf.tensorlib` shim layer between the different backends

# %%
pyhf.tensorlib

# %%
pyhf.get_backend()

# %% [markdown]
# revising the `pyhf` tensor libarires to work with `array-api-compat` means that the tensor backends could become plugins in the future.
#
# If users have an array library that impliments the Python array API standard they could impliment the tensor backend themselves.
#
# Possible to also focus more on optimization.

# %% [markdown]
# ✨ **Checkout [Jack Araz's talk on Friday on Spey](https://indico.cern.ch/event/1252095/timetable/#8-spey-smooth-inference-for-re)**

# %% [markdown]
# Other tools, like [Spey](https://speysidehep.github.io/spey/), are already using plugins to be able to use `pyhf` as an optional backend with [`spey-pyhf`](https://speysidehep.github.io/spey-pyhf/quick_start.html).
#
# ```
# python -m pip install --upgrade spey spey-pyhf
# ```

# %%
import spey
print(spey.AvailableBackends())

# %% [markdown]
# ## [HEP Statistics Serialization Standard](https://github.com/hep-statistics-serialization-standard/hep-statistics-serialization-standard) (HS3)

# %% [markdown]
# [![hs3-readme](figures/hs3-readme.png)](https://github.com/hep-statistics-serialization-standard/hep-statistics-serialization-standard)

# %% [markdown]
# ## [`pyhf` Users and Developers Workshop 2023](https://indico.cern.ch/event/1294577/)

# %% [markdown]
# If you're like to learn more about `pyhf` or get involved with development, we'd encourage you to participate in the upcoming `pyhf` workshop at CERN (4 - 8th, December, 2023).

# %% [markdown]
# [![pyhf-workshop-indico](figures/pyhf-workshop-indico.png)](https://indico.cern.ch/event/1294577/)
