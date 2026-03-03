# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyEsda(PythonPackage):
    """Exploratory Spatial Data Analysis in PySAL"""

    homepage = "https://pysal.org/esda/"
    pypi = "esda/esda-2.6.0-py3-none-any.whl"

    version("1.0.0.dev0", sha256="9bdaad6c7f5f7820854a76cf926d0c0e941c0dd2b3c6beff2b21a0c303f1a846")
    version("1.0.1.dev0", sha256="a3619f39703bf0541e290824a692d4dea5a6d4af02f98ae1e11b7dccc6075941")
    version("2.0.0", sha256="d074e303c8124bbd9c5a086bf95c2995c8ebc937ac678fcde0f4e3abe4092f05")
    version("2.1.0", sha256="f5e7299c061fba430cb716039b5319a30b45edb34c426482bfec6648323d8570")
    version("2.1.1", sha256="abecd2e33bf9b856e57b103de989e6b7a18391d9dcd8bc1a75f494af260405d4")
    version("2.2.0", sha256="418a210a9c865fb56637c1e489ffc300bade046588dc47b322f2d39c8720f669")
    version("2.2.1", sha256="59569f6a9068522adb7e71848956532018a037ad6791bbd593f049c10d7dae68")
    version("2.3.0", sha256="70def8ff4f571e14e8c9bce669de2d02bbfc336d7d31eb7d942d17ddda3dd9ac")
    version("2.3.1", sha256="2a53825636e037127e4e1ab7213207d217019e56171be558d5fe76202b47f082")
    version(
        "2.3.2",
        sha256="72237a79fe55572a75ed4006b4b4b7ccdc2345dd2a5c9cc7a012e24979e098cd",
        expand=False,
        url="https://files.pythonhosted.org/packages/44/79/227f5fa4aa5a6eb29e41d0322c3fd0ef13a2eb690b49de794d689dd278ab/esda-2.3.2-py3-none-any.whl",
    )
    version(
        "2.3.5",
        sha256="6ff995b15de901680439510d57c5e3a5055f1a34aa17293d45d669ac44fb9c12",
        expand=False,
        url="https://files.pythonhosted.org/packages/68/b7/35bcafb2e12c99b0b26b2a6bf78bf6b448757d8f5eb47b6b2965635c9a63/esda-2.3.5-py3-none-any.whl",
    )
    version(
        "2.3.6",
        sha256="1cd8d60e6d492587601a03863e6f5fede55b4c54ea432ae8b4446d46ccf204f8",
        expand=False,
        url="https://files.pythonhosted.org/packages/20/02/7c36f3c7c22f048f50ada6402ff3fbe51e0c5365f7d0227196b84d43c82b/esda-2.3.6-py3-none-any.whl",
    )
    version("2.4.0", sha256="440d2b9343485a042768821aa5dbc3ec51ca6eb8ced69872efbf0a61f0af10ed")
    version("2.4.1", sha256="308b43cdc2f7af9b01c4a71fb1869092d48bcdf953e99dba8fc8239745779f1e")
    version("2.4.3", sha256="a7c98e3205b3318a0acc7a278e31a734bbf66843b8722563cc22934c537978ff")
    version(
        "2.5.0",
        sha256="d43caa6cc01945aacab6a2ea39cbebffd6146308b29b95af913d5f42245d8052",
        expand=False,
        url="https://files.pythonhosted.org/packages/13/d3/1b1c2685f638c0bd4f7bd83cf8b3e0b9e2f3e8c92c9268794731d91b811e/esda-2.5.0-py3-none-any.whl",
    )
    version(
        "2.5.1",
        sha256="6fdbce49e8ef39feeca7ab0f92cd1d8f1ddda527425c42e61d0e8199b70bc8e8",
        expand=False,
        url="https://files.pythonhosted.org/packages/ea/e1/6000a61d9a964dbb592db8271232693ef2e341d088c7bdf9393a9a34b658/esda-2.5.1-py3-none-any.whl",
    )
    version(
        "2.6.0",
        sha256="d825247f1e3dd7bf63e59835989d934a5edc03ece6cb816bbccb3cd9a3f313fc",
        expand=False,
        url="https://files.pythonhosted.org/packages/a0/1b/84eaa84fa0e2b56464665f1d2135e0afe8ab1df481e6aa1fcdcb480032d6/esda-2.6.0-py3-none-any.whl",
    )

    depends_on("py-setuptools", type=("build"))
    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-geopandas", type=("build", "run"))
    depends_on("py-libpysal", type=("build", "run"))
    depends_on("py-libpysal@4.12:", type=("build", "run"), when="@2.6.0:")
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-pandas", type=("build", "run"))
    depends_on("py-scikit-learn", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-shapely", type=("build", "run"))


# {'scipy(>=0.11)': ['2.3.2', '2.3.5', '2.3.6'], 'pandas': ['2.3.2', '2.3.5', '2.3.6'], 'libpysal': ['2.3.2', '2.3.5', '2.3.6', '2.5.0', '2.5.1'], 'scikit-learn': ['2.3.2', '2.3.5', '2.3.6'], "sphinx(>=1.4.3);extra=='docs'": ['2.3.2', '2.3.5', '2.3.6'], "sphinxcontrib-napoleon;extra=='docs'": ['2.3.2', '2.3.5', '2.3.6'], "sphinx-gallery;extra=='docs'": ['2.3.2', '2.3.5', '2.3.6'], "sphinxcontrib-bibtex;extra=='docs'": ['2.3.2', '2.3.5', '2.3.6', '2.5.0', '2.5.1', '2.6.0'], "sphinx-bootstrap-theme;extra=='docs'": ['2.3.2', '2.3.5', '2.3.6', '2.5.0', '2.5.1', '2.6.0'], "numpydoc;extra=='docs'": ['2.3.2', '2.3.5', '2.3.6', '2.5.0', '2.5.1', '2.6.0'], "numba;extra=='plus'": ['2.3.2', '2.3.5', '2.3.6'], "geopandas;extra=='tests'": ['2.3.2', '2.3.5', '2.3.6', '2.5.0', '2.5.1'], "pytest;extra=='tests'": ['2.3.2', '2.3.5', '2.3.6', '2.5.0', '2.5.1', '2.6.0'], "pytest-cov;extra=='tests'": ['2.3.2', '2.3.5', '2.3.6', '2.5.0', '2.5.1', '2.6.0'], "codecov;extra=='tests'": ['2.3.2', '2.3.5', '2.3.6', '2.5.0', '2.5.1', '2.6.0'], "twine;extra=='tests'": ['2.3.2', '2.3.5', '2.3.6'], 'pandas>1.4': ['2.5.0', '2.5.1'], 'scikit-learn>=1.0': ['2.5.0', '2.5.1'], 'scipy>=1.9': ['2.5.0', '2.5.1', '2.6.0'], "pre-commit;extra=='dev'": ['2.5.0', '2.5.1', '2.6.0'], "nbsphinx;extra=='docs'": ['2.5.0', '2.5.1', '2.6.0'], "pandoc;extra=='docs'": ['2.5.0', '2.5.1', '2.6.0'], "sphinx;extra=='docs'": ['2.5.0', '2.5.1', '2.6.0'], "folium;extra=='notebooks'": ['2.5.0', '2.5.1'], "matplotlib;extra=='notebooks'": ['2.5.0', '2.5.1'], "matplotlib-scalebar;extra=='notebooks'": ['2.5.0', '2.5.1', '2.6.0'], "seaborn;extra=='notebooks'": ['2.5.0', '2.5.1', '2.6.0'], "watermark;extra=='notebooks'": ['2.5.0', '2.5.1', '2.6.0'], "coverage;extra=='tests'": ['2.5.0', '2.5.1'], "pytest-xdist;extra=='tests'": ['2.5.0', '2.5.1', '2.6.0'], 'geopandas>=0.12': ['2.6.0'], 'libpysal>=4.12': ['2.6.0'], 'numpy>=1.24': ['2.6.0'], 'pandas>1.5': ['2.6.0'], 'scikit-learn>=1.2': ['2.6.0'], 'shapely>=2.0': ['2.6.0'], "ruff;extra=='dev'": ['2.6.0'], "numba>=0.57;extra=='plus'": ['2.6.0'], "rtree>=1.0;extra=='plus'": ['2.6.0'], "folium;extra=='tests'": ['2.6.0'], "mapclassify;extra=='tests'": ['2.6.0'], "matplotlib;extra=='tests'": ['2.6.0']}
