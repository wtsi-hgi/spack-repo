# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyScglue(PythonPackage):
    """Graph-linked unified embedding for unpaired single-cell multi-omics data integration"""
    
    homepage = "None"
    pypi = "scglue/scglue-0.3.2-py3-none-any.whl" 

    version("0.1.1", sha256="4f0cd56755b685e2cc7adf9988cdf799242f8be262fcd6253d83e14c20776b4e", expand=False, url="https://files.pythonhosted.org/packages/7e/d0/5f9175ded8d8db1b323b3aebc5695ea8056125f7e6fa8c5e2b3621f6fbe0/scglue-0.1.1-py3-none-any.whl")
    version("0.2.0", sha256="79054762a15628fd82a2f68a1e16f9b277031c417c74b198ce86863fb93abe5e", expand=False, url="https://files.pythonhosted.org/packages/24/6d/d727130c1900e34026598182ac7693c0a669c4cd1f6346342c1055a1d1dd/scglue-0.2.0-py3-none-any.whl")
    version("0.2.1", sha256="3fa9177aa59228222933def37fb52dd12cf363bfc3ebc7a1bb3104b495533b58", expand=False, url="https://files.pythonhosted.org/packages/34/ba/77caf5880f6f0a6110f0265fad87398479c1d8e9c18fbd4ef640c07a1efa/scglue-0.2.1-py3-none-any.whl")
    version("0.2.2", sha256="2feb56b9ecf4b47780af3cce595bad28f17fdb24a2ef5fac65652c2941cb76a5", expand=False, url="https://files.pythonhosted.org/packages/3c/c3/ee997e00966574c2a09f1e0ebf7225e97983d05a24dbbf7a38ab9c89d857/scglue-0.2.2-py3-none-any.whl")
    version("0.2.3", sha256="2c2a3466d08a94533774cd5495bce1dc88a2e40e8bd9cdb951c87b605ff99b46", expand=False, url="https://files.pythonhosted.org/packages/d3/c3/5f57c00d7a8de9d19b4acc6cc083a82c77bfacdf70845f008a1d1ce4c818/scglue-0.2.3-py3-none-any.whl")
    version("0.3.0", sha256="d5cdc19be098f8b3f741500e37abacafdf7bae96d40f4587b24afba195e03cd6", expand=False, url="https://files.pythonhosted.org/packages/d1/47/7f5ba6e5b1acf477230d35a65f30b22b6ebc1dfd949660a6ffa6a0e807ee/scglue-0.3.0-py3-none-any.whl")
    version("0.3.1", sha256="39889a55c76d92fbdef23eca305c0fcbc3327d693e0eab6cc82bad666953fb0b", expand=False, url="https://files.pythonhosted.org/packages/25/e5/342e0e091396b166fa695239c577da22b69e1ecdaf40b3b2905f42762111/scglue-0.3.1-py3-none-any.whl")
    version("0.3.2", sha256="efec4e3f8cc3ffce362e180e4912327d4aacc2dd0a76a6cb06e851a426695d6d", expand=False, url="https://files.pythonhosted.org/packages/dc/97/d4730124de7edb1be55b48bbcb7057587708ca52d0a75bca275969969cd4/scglue-0.3.2-py3-none-any.whl")

    depends_on("py-setuptools", type=("build"))
    depends_on("python@3.6:", type=("build", "run"))
    depends_on("py-torch", type=("build", "run"))
    depends_on("py-tqdm", type=("build", "run"))
    depends_on("py-pynvml", type=("build", "run"))
    depends_on("py-pybedtools", type=("build", "run"))
    depends_on("py-leidenalg", type=("build", "run"))
    depends_on("py-parse", type=("build", "run"))
    depends_on("py-scanpy", type=("build", "run"))
    depends_on("py-networkx", type=("build", "run"))
    depends_on("py-scikit-learn", type=("build", "run"))
    depends_on("py-dill", type=("build", "run"))
    depends_on("py-pytorch-ignite", type=("build", "run"))
    depends_on("py-tensorboardx", type=("build", "run"))
    depends_on("py-sparse", type=("build", "run"))
    depends_on("py-matplotlib", type=("build", "run"))
    depends_on("py-statsmodels", type=("build", "run"))
    depends_on("py-anndata", type=("build", "run"))
    depends_on("py-pandas", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-packaging", type=("build", "run"))
    depends_on("py-seaborn", type=("build", "run"))
    depends_on("py-h5py", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))

# {'numpy>=1.19': ['0.1.1', '0.2.0', '0.2.1', '0.2.2', '0.2.3', '0.3.0', '0.3.1', '0.3.2'], 'scipy>=1.3': ['0.1.1', '0.2.0', '0.2.1', '0.2.2', '0.2.3', '0.3.0', '0.3.1', '0.3.2'], 'pandas>=1.1': ['0.1.1', '0.2.0', '0.2.1', '0.2.2', '0.2.3', '0.3.0', '0.3.1', '0.3.2'], 'matplotlib>=3.1.2': ['0.1.1', '0.2.0', '0.2.1', '0.2.2', '0.2.3', '0.3.0', '0.3.1', '0.3.2'], 'seaborn>=0.9': ['0.1.1', '0.2.0', '0.2.1', '0.2.2', '0.2.3', '0.3.0', '0.3.1', '0.3.2'], 'dill>=0.2.3': ['0.1.1', '0.2.0', '0.2.1', '0.2.2', '0.2.3', '0.3.0', '0.3.1', '0.3.2'], 'tqdm>=4.27': ['0.1.1', '0.2.0', '0.2.1', '0.2.2', '0.2.3', '0.3.0', '0.3.1', '0.3.2'], 'scikit-learn>=0.21.2': ['0.1.1', '0.2.0', '0.2.1', '0.2.2', '0.2.3', '0.3.0', '0.3.1', '0.3.2'], 'statsmodels>=0.10': ['0.1.1', '0.2.0', '0.2.1', '0.2.2', '0.2.3', '0.3.0', '0.3.1', '0.3.2'], 'parse>=1.3.2': ['0.1.1', '0.2.0', '0.2.1', '0.2.2', '0.2.3', '0.3.0', '0.3.1', '0.3.2'], 'networkx>=2': ['0.1.1', '0.2.0', '0.2.1', '0.2.2', '0.2.3', '0.3.0', '0.3.1', '0.3.2'], 'pynvml>=8.0.1': ['0.1.1', '0.2.0', '0.2.1', '0.2.2', '0.2.3', '0.3.0', '0.3.1', '0.3.2'], 'torch>=1.7': ['0.1.1', '0.2.0'], 'pytorch-ignite>=0.4.1': ['0.1.1', '0.2.0', '0.2.1', '0.2.2', '0.2.3', '0.3.0', '0.3.1', '0.3.2'], 'tensorboardX>=1.4': ['0.1.1', '0.2.0', '0.2.1', '0.2.2', '0.2.3', '0.3.0', '0.3.1', '0.3.2'], 'anndata>=0.7': ['0.1.1', '0.2.0', '0.2.1', '0.2.2', '0.2.3', '0.3.0', '0.3.1', '0.3.2'], 'scanpy>=1.5': ['0.1.1', '0.2.0', '0.2.1', '0.2.2', '0.2.3', '0.3.0', '0.3.1', '0.3.2'], 'pybedtools>=0.8.1': ['0.1.1', '0.2.0', '0.2.1', '0.2.2', '0.2.3', '0.3.0', '0.3.1', '0.3.2'], 'sphinx<4;extra=="doc"': ['0.1.1', '0.2.0', '0.2.1', '0.2.2', '0.2.3'], 'sphinx-autodoc-typehints<1.12;extra=="doc"': ['0.1.1', '0.2.0', '0.2.1', '0.2.2', '0.2.3'], 'sphinx-copybutton;extra=="doc"': ['0.1.1', '0.2.0', '0.2.1', '0.2.2', '0.2.3', '0.3.0', '0.3.1', '0.3.2'], 'nbsphinx;extra=="doc"': ['0.1.1', '0.2.0', '0.2.1', '0.2.2', '0.2.3', '0.3.0', '0.3.1', '0.3.2'], 'sphinx-rtd-theme;extra=="doc"': ['0.1.1', '0.2.0', '0.2.1', '0.2.2', '0.2.3', '0.3.0', '0.3.1', '0.3.2'], 'ipython;extra=="doc"': ['0.1.1', '0.2.0', '0.2.1', '0.2.2', '0.2.3', '0.3.0', '0.3.1', '0.3.2'], 'flake8;extra=="test"': ['0.1.1'], 'pytest;extra=="test"': ['0.1.1', '0.2.0', '0.2.1', '0.2.2', '0.2.3', '0.3.0', '0.3.1', '0.3.2'], 'pytest-cov;extra=="test"': ['0.1.1', '0.2.0', '0.2.1', '0.2.2', '0.2.3', '0.3.0', '0.3.1', '0.3.2'], 'h5py': ['0.2.0'], 'sparse': ['0.2.0'], 'packaging': ['0.2.0'], 'leidenalg;extra=="test"': ['0.2.0'], 'plotly;extra=="test"': ['0.2.0', '0.2.1', '0.2.2', '0.2.3', '0.3.0', '0.3.1', '0.3.2'], 'torch>=1.8': ['0.2.1', '0.2.2', '0.2.3', '0.3.0', '0.3.1', '0.3.2'], 'h5py>=2.10': ['0.2.1', '0.2.2', '0.2.3', '0.3.0', '0.3.1', '0.3.2'], 'sparse>=0.3.1': ['0.2.1', '0.2.2', '0.2.3', '0.3.0', '0.3.1', '0.3.2'], 'packaging>=16.8': ['0.2.1', '0.2.2', '0.2.3', '0.3.0', '0.3.1', '0.3.2'], 'leidenalg>=0.7': ['0.2.1', '0.2.2', '0.2.3', '0.3.0', '0.3.1', '0.3.2'], 'jinja2<3.1;extra=="doc"': ['0.2.1', '0.2.2', '0.2.3'], 'sphinx;extra=="doc"': ['0.3.0', '0.3.1', '0.3.2'], 'sphinx-autodoc-typehints;extra=="doc"': ['0.3.0', '0.3.1', '0.3.2'], 'sphinx-intl;extra=="doc"': ['0.3.0', '0.3.1', '0.3.2'], 'jinja2;extra=="doc"': ['0.3.0', '0.3.1', '0.3.2']}