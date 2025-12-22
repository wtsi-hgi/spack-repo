# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyHucira(PythonPackage):
    """huCIRA (human Cytokine Immune Response Analysis) provides an easy-to-use interface to analyze cytokine signaling and cytokine-induced immune program enrichment in transcriptomic datasets."""
    
    homepage = "https://github.com/theislab/huCIRA"
    pypi = "huCIRA/hucira-0.1.1-py3-none-any.whl"

    license("MIT")

    version("0.0.1", sha256="a297db4ceda26f75e5bdf3ae81535b6bd078dcab747e33266799e333067a9352", expand=False, url="https://files.pythonhosted.org/packages/3a/35/8e62c50e9683aa2735af1ee254649da0c64013c8e4fc076cd9a8fd6fade5/hucira-0.0.1-py3-none-any.whl")
    version("0.1.0", sha256="a825497211f95fceb705a5722ef7ce138b1294d189d99dac3a84f8dc23baa12f", expand=False, url="https://files.pythonhosted.org/packages/3b/ec/4274122894ec10127d573b5dd66393324f34aed2f2d8b477654528fbc5b3/hucira-0.1.0-py3-none-any.whl")
    version("0.1.1", sha256="960f1c0ea8ca107585f9b3b728492b1d5bd0521ec719abd2bdf74561d6e0c8db", expand=False, url="https://files.pythonhosted.org/packages/8d/17/4437ba5f78d4df8779f43c910d6175c14c0f6f651e75088b0605731fd052/hucira-0.1.1-py3-none-any.whl")

    depends_on("py-setuptools", type=("build"))
    depends_on("python@3.11:", type=("build", "run"))
    depends_on("py-anndata", type=("build", "run"))
    depends_on("py-bokeh", type=("build", "run"))
    depends_on("py-gseapy", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-openpyxl", type=("build", "run"))
    depends_on("py-pandas", type=("build", "run"))
    depends_on("py-pycirclize", type=("build", "run"))
    depends_on("py-scanpy", type=("build", "run"))
    depends_on("py-scikit-learn", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-seaborn", type=("build", "run"))
    depends_on("py-session-info2", type=("build", "run"))
    depends_on("py-tqdm", type=("build", "run"))
    depends_on("py-ipython", type=("build", "run"))

# {'anndata': ['0.0.1', '0.1.0', '0.1.1'], 'anndata>=0.11.4': ['0.0.1'], 'bokeh': ['0.0.1', '0.1.0', '0.1.1'], 'gseapy>=1.1.8': ['0.0.1', '0.1.0', '0.1.1'], 'numpy>=2.1': ['0.0.1', '0.1.0', '0.1.1'], 'openpyxl': ['0.0.1', '0.1.0', '0.1.1'], 'pandas>=2.2.3': ['0.0.1', '0.1.0', '0.1.1'], 'pycirclize': ['0.0.1', '0.1.0', '0.1.1'], 'scanpy>=1.11.1': ['0.0.1', '0.1.0', '0.1.1'], 'scikit-learn>=1.5.2': ['0.0.1', '0.1.0', '0.1.1'], 'scipy>=1.15.2': ['0.0.1', '0.1.0', '0.1.1'], 'seaborn>=0.13.2': ['0.0.1', '0.1.0', '0.1.1'], 'session-info2': ['0.0.1', '0.1.0', '0.1.1'], 'tqdm>=4.67.1': ['0.0.1', '0.1.0', '0.1.1'], "pre-commit;extra=='dev'": ['0.0.1', '0.1.0', '0.1.1'], "twine>=4.0.2;extra=='dev'": ['0.0.1', '0.1.0', '0.1.1'], "docutils!=0.18.*,!=0.19.*,>=0.8;extra=='doc'": ['0.0.1', '0.1.0', '0.1.1'], "ipykernel;extra=='doc'": ['0.0.1', '0.1.0', '0.1.1'], "ipython;extra=='doc'": ['0.0.1', '0.1.0', '0.1.1'], "myst-nb>=1.1;extra=='doc'": ['0.0.1', '0.1.0', '0.1.1'], "pandas;extra=='doc'": ['0.0.1', '0.1.0', '0.1.1'], "setuptools;extra=='doc'": ['0.0.1', '0.1.0', '0.1.1'], "sphinx-autodoc-typehints;extra=='doc'": ['0.0.1', '0.1.0', '0.1.1'], "sphinx-book-theme>=1;extra=='doc'": ['0.0.1', '0.1.0', '0.1.1'], "sphinx-copybutton;extra=='doc'": ['0.0.1', '0.1.0', '0.1.1'], "sphinx-tabs;extra=='doc'": ['0.0.1', '0.1.0', '0.1.1'], "sphinx>=8.1;extra=='doc'": ['0.0.1', '0.1.0', '0.1.1'], "sphinxcontrib-bibtex>=1;extra=='doc'": ['0.0.1', '0.1.0', '0.1.1'], "sphinxcontrib-katex;extra=='doc'": ['0.0.1', '0.1.0', '0.1.1'], "sphinxext-opengraph;extra=='doc'": ['0.0.1', '0.1.0', '0.1.1'], "coverage>=7.10;extra=='test'": ['0.0.1', '0.1.0', '0.1.1'], "ipython;extra=='test'": ['0.0.1', '0.1.0', '0.1.1'], "pytest;extra=='test'": ['0.0.1', '0.1.0', '0.1.1']}