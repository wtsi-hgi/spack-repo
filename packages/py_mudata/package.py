# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyMudata(PythonPackage):
	"""Multimodal data"""
	
	homepage = "https://mudata.rtfd.io"
	pypi = "mudata/mudata-0.3.2-py3-none-any.whl" 

	version("0.0.1", sha256="16804b5499f9d32cdaf968bfbe59079c2364b3116e0d0375a29f6f8224594e1d", expand=False, url="https://files.pythonhosted.org/packages/e4/4e/5518dabd10f9ea5c4fe10be26a09d26cdd1ae0df264f51c34733c837f19f/mudata-0.0.1-py3-none-any.whl")
	version("0.0.9", sha256="87ccae3be46dcf5442f9fe232c54b32be8433008cc3142ee7d50a8d7a69eb1d8", expand=False, url="https://files.pythonhosted.org/packages/e0/19/032c6fc9f650bf24e02f39c9bfe5b5d77c39aee8df9ecea078ea1ab41c30/mudata-0.0.9-py3-none-any.whl")
	version("0.1.0", sha256="0709f09f19de1c81359f69b164eda3b7b7ad9fb7cecf97e1e84980a3be355260", expand=False, url="https://files.pythonhosted.org/packages/fe/26/ae7fbd2aa7f2c4307e0136f2e3dd23bc5164acbe31049e5810cbdc36c9fc/mudata-0.1.0-py3-none-any.whl")
	version("0.1.1", sha256="a6b545954e93d0c84386993c0ec05076441239fa227acd47dea204a45ebafc50", expand=False, url="https://files.pythonhosted.org/packages/78/31/22f55d39d88092bf0450fcffaf47c66eeba14479cf2360602b6a45971b92/mudata-0.1.1-py3-none-any.whl")
	version("0.1.2", sha256="d7dcd046398193405e407ef3f8158ffb934e916db4c346d7792623f51ff15dfd", expand=False, url="https://files.pythonhosted.org/packages/78/b5/8f9cfcdc842e7b9ec50ae35f4e1b7e6ae88614d376b9f6b9c4f3371ae63c/mudata-0.1.2-py3-none-any.whl")
	version("0.2.0", sha256="d4453c00cee218930d7e3c78df146f478ef16a930eb398299f78ab8f71d5b47b", expand=False, url="https://files.pythonhosted.org/packages/70/cc/804e8c6945ed11657e12adb34d4b8bd84f16a8b02990bf4fe74085185772/mudata-0.2.0-py3-none-any.whl")
	version("0.2.1", sha256="12cc6204e178a2dde51ade2f5c0b2c558aa71f6840298a879c52966d1a203173", expand=False, url="https://files.pythonhosted.org/packages/22/38/e5e02c8749ebb9a788ee0a184099de63c510bad7842017b2f478a1820b8f/mudata-0.2.1-py3-none-any.whl")
	version("0.2.2", sha256="35518078be7a041de761a93ed8ac3d5a252dd22a34ad78cc1a9924ca1cd5651c", expand=False, url="https://files.pythonhosted.org/packages/fc/a4/3e44152a9b58573ec749219567a718ec5983c05addee72b77609b225e09f/mudata-0.2.2-py3-none-any.whl")
	version("0.2.3", sha256="39f234b5943d800d30622009e448189fbc635b6f9b51b985f9e6926b313ea7a0", expand=False, url="https://files.pythonhosted.org/packages/c2/9f/ba965a5b0092f1bb76f969afd6343f53634bdb72890f432f74d410b47d8f/mudata-0.2.3-py3-none-any.whl")
	version("0.2.4", sha256="d4dd670d1470dbdb2a2c9d49df82862ee01e58ed01fa8184d495ce5b01aafef7", expand=False, url="https://files.pythonhosted.org/packages/4e/16/15ab8062940291b7ee18cca0a3ad328b1463724ce3989a3d48979c1cd856/mudata-0.2.4-py3-none-any.whl")
	version("0.3.0", sha256="035a1bbf94ee40308d12aae6f13fcba9a9b43d71786045d7f1437967a28d7514", expand=False, url="https://files.pythonhosted.org/packages/0f/aa/9d0231e6cdf05a4b318e0d148b114991cd584217206063e276541b618a02/mudata-0.3.0-py3-none-any.whl")
	version("0.3.0rc0", sha256="af1068318e4559bb0859d45c41dbd3c4f7caffa20ba03ea6d311d1c30029dccb", expand=False, url="https://files.pythonhosted.org/packages/a0/80/573f0d5ac00c787ccf0d70b381c2c10ba02a81ffc7183349141b4a96bce5/mudata-0.3.0rc0-py3-none-any.whl")
	version("0.3.1", sha256="d3a5ce96c3fcb64077be936758cc71657475905a4bbeeeba17c9ff48173f6c9d", expand=False, url="https://files.pythonhosted.org/packages/96/10/7b9588eee1883c269453b44d643ae68e37c93eb78f7b6bdd2838688e957c/mudata-0.3.1-py3-none-any.whl")
	version("0.3.2", sha256="185b80b61993515a121258401932db877bc123ba2677cdbd87051e974dfcd897", expand=False, url="https://files.pythonhosted.org/packages/3f/de/f7bf1832967e7e4bcd34b232ed33169a0d86a8efbcdc7fcfd8f98c18d5c1/mudata-0.3.2-py3-none-any.whl")

	depends_on("py-setuptools", type=("build"))
	depends_on("python@3.10:", type=("build", "run"))
	depends_on("py-numpy", type=("build", "run"))
	depends_on("py-pandas", type=("build", "run"))
	depends_on("py-h5py", type=("build", "run"))
	depends_on("py-anndata@:0.7", type=("build", "run"), when="@0.0.9:0.1.0")
	depends_on("py-anndata@:0.7", type=("build", "run"), when="@0.1.1:0.1.2")
	depends_on("py-anndata@0.8:", type=("build", "run"), when="@0.2.0:0.2.3")
	depends_on("py-anndata@0.10.8:", type=("build", "run"), when="@0.2.4:")

# {'numpy': ['0.0.9', '0.1.0', '0.1.1', '0.1.2', '0.2.0', '0.2.1', '0.2.2', '0.2.3', '0.2.4'], 'pandas': ['0.0.9', '0.1.0', '0.1.1', '0.1.2', '0.2.0', '0.2.1', '0.2.2', '0.2.3', '0.2.4'], 'h5py': ['0.0.9', '0.1.0', '0.1.1', '0.1.2', '0.2.0', '0.2.1', '0.2.2', '0.2.3', '0.2.4'], 'anndata': ['0.0.9', '0.1.0'], 'sphinx>=4.0;extra=="docs"': ['0.0.9', '0.1.0', '0.1.1', '0.1.2', '0.2.0', '0.2.1', '0.2.2', '0.2.3'], 'sphinx-rtd-theme;extra=="docs"': ['0.0.9', '0.1.0', '0.1.1'], 'readthedocs-sphinx-search;extra=="docs"': ['0.0.9', '0.1.0', '0.1.1', '0.1.2', '0.2.0', '0.2.1', '0.2.2', '0.2.3', '0.2.4'], 'nbsphinx;extra=="docs"': ['0.0.9', '0.1.0', '0.1.1', '0.1.2', '0.2.0', '0.2.1', '0.2.2', '0.2.3', '0.2.4'], 'sphinx_automodapi;extra=="docs"': ['0.0.9', '0.1.0', '0.1.1', '0.1.2', '0.2.0', '0.2.1', '0.2.2', '0.2.3', '0.2.4'], 'anndata<0.8': ['0.1.1', '0.1.2'], 'sphinx-book-theme;extra=="docs"': ['0.1.2', '0.2.0', '0.2.1', '0.2.4'], 'zarr;extra=="test"': ['0.1.2', '0.2.0', '0.2.1', '0.2.2', '0.2.3', '0.2.4'], 'anndata>=0.8': ['0.2.0', '0.2.1', '0.2.2', '0.2.3'], 'sphinx-book-theme==0.3.3;extra=="docs"': ['0.2.2', '0.2.3'], 'pydata-sphinx-theme==0.8.1;extra=="docs"': ['0.2.2', '0.2.3'], 'anndata>=0.10.8': ['0.2.4', '0.3.0', '0.3.0rc0', '0.3.1', '0.3.2'], 'sphinx;extra=="docs"': ['0.2.4'], 'pydata-sphinx-theme;extra=="docs"': ['0.2.4'], 'recommonmark;extra=="docs"': ['0.2.4'], "setuptools-scm;extra=='dev'": ['0.3.0', '0.3.0rc0', '0.3.1', '0.3.2'], "nbsphinx;extra=='docs'": ['0.3.0', '0.3.0rc0', '0.3.1', '0.3.2'], "pydata-sphinx-theme;extra=='docs'": ['0.3.0', '0.3.0rc0', '0.3.1', '0.3.2'], "readthedocs-sphinx-search;extra=='docs'": ['0.3.0', '0.3.0rc0', '0.3.1', '0.3.2'], "recommonmark;extra=='docs'": ['0.3.0', '0.3.0rc0', '0.3.1', '0.3.2'], "sphinx;extra=='docs'": ['0.3.0', '0.3.0rc0', '0.3.1', '0.3.2'], "sphinx-automodapi;extra=='docs'": ['0.3.0', '0.3.0rc0', '0.3.1', '0.3.2'], "sphinx-book-theme;extra=='docs'": ['0.3.0', '0.3.0rc0', '0.3.1', '0.3.2'], "zarr;extra=='test'": ['0.3.0', '0.3.0rc0', '0.3.1'], "pytest;extra=='test'": ['0.3.2'], "zarr<3;extra=='test'": ['0.3.2']}