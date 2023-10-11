# %% [markdown]
# # [PyHEP 2023: `pyhf` upcoming features and development](https://indico.cern.ch/event/1252095/contributions/5592418/)

# %%
import pyhf
import jax
import cabinetry

# %% [markdown]
# ## `pyhf` `v0.8.0rc1` coming soon

# %% [markdown]
# Aim was to have a release candidate up for PyHEP 2023, but didn't hit quite hit that.

# %% [markdown]
# ## Ecosystem extensions

# %% [markdown]
# ✨ **checkout [Malin Horstmann's talk on Wednesday on Bayesian and frequentist methodologies with `pyhf`](https://indico.cern.ch/event/1252095/timetable/#19-bayesian-and-frequentist-me)**

# %%
import Bayesian_pyhf

# %% [markdown]
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
# ✨ **checkout [Jack Araz's talk on Friday on Spey](https://indico.cern.ch/event/1252095/timetable/#8-spey-smooth-inference-for-re)**

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
