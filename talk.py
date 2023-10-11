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
# and then from
#
# ```python
# import pyhf
# pyhf.bayes  # this isn't a real API, just an example of an idea
# ```
#
# would work.

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
