# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPegg(PythonPackage):
	"""Prime Editing Guide Generator"""
	
	homepage = "https://github.com/samgould2/PEGG2.0"
	pypi = "pegg/pegg-2.1.0-py3-none-any.whl" 

	version("0.0.1", sha256="02e5c3b78045c93cbe4aa0d6e0bc00d69783b306a07e1c6252d1dbeabdfc954b", expand=False, url="https://files.pythonhosted.org/packages/55/89/1cabc55549b3d505ba6611bb27e071f0f25b505c83bcfea20cb29d05ec7b/pegg-0.0.1-py3-none-any.whl")
	version("1.0.0", sha256="5d8a4e14a21491fd670bac09150882ed6329bbb94f02b13e22597fac9cf1e1bb", expand=False, url="https://files.pythonhosted.org/packages/64/ef/6189320c4a4707f35702d410e962b9250a2c523efa6c854d03a0b4268d7b/pegg-1.0.0-py3-none-any.whl")
	version("1.0.1", sha256="6f72491e9ccaa312d4c45ea5f45c10c5904d72903805eb322b84d553b0a35d47", expand=False, url="https://files.pythonhosted.org/packages/63/c3/d7878e1354e07c1e4345e886525c15b3c181d6d24a220484c51564a4232f/pegg-1.0.1-py3-none-any.whl")
	version("1.0.2", sha256="ffb91ffe4f46d76f2259ffc237c3dae3010c8992b8d9a00ba59fb95cd16a72d6", expand=False, url="https://files.pythonhosted.org/packages/20/46/a526f75c56e0da014427cc9bdbfec564b81f7d22f13bd2387c8d3175fa11/pegg-1.0.2-py3-none-any.whl")
	version("1.0.4", sha256="4c119731106a30a25e4065280e3e1b9fca20b82ee163cb7f42c624788204af59", expand=False, url="https://files.pythonhosted.org/packages/68/af/fb7e68da77fe4d6c754ca5c1ae6f0401b1b0ee4c1065fa28509f50efaf09/pegg-1.0.4-py3-none-any.whl")
	version("1.0.5", sha256="8ceb27d54321e5f0a451d2ee730160f1d2bfa3b1bc6633de831dc7653ea8508e", expand=False, url="https://files.pythonhosted.org/packages/b8/4c/11f8ab1673f290d3f52ea3f7cf9a4006d0051ca52eb505d878f5b568c121/pegg-1.0.5-py3-none-any.whl")
	version("1.0.6", sha256="1f1e68d6fbe5569a89fe975f1c9b4d8ec1822cbc9b700db996d712952910b90c", expand=False, url="https://files.pythonhosted.org/packages/c2/fd/1f8abbfe38e5661ecd59729add8566f433d43a8585239fda71526fec6f2e/pegg-1.0.6-py3-none-any.whl")
	version("2.0.8", sha256="06cf8960ed18263aa584c46b83b4c60e311196b51d4b90d98326fea4a62d7f1c", expand=False, url="https://files.pythonhosted.org/packages/5b/b4/0c505805f019d8a1b3162cb6d97cb1fcd5330fdf928b708c9a10391da3bc/pegg-2.0.8-py3-none-any.whl")
	version("2.0.9", sha256="7f05b2b6b7ffbf484818811df1e6adcf5ff578efc80e73462eb01835b851aa2d", expand=False, url="https://files.pythonhosted.org/packages/7a/b8/910745b6c1f91b3f21ae3478fd0a8ba6c6fd53ede3cf3674fae38e3f7400/pegg-2.0.9-py3-none-any.whl")
	version("2.1.0", sha256="4fa00989b9795ae047b44afb996baf6bdeb0c33faa546d9bd17603294729c019", expand=False, url="https://files.pythonhosted.org/packages/1e/9d/93ea667f8573bf13ddad2b7f28ddd966a3f43aba51ab00ac8802fb75aca5/pegg-2.1.0-py3-none-any.whl")

	depends_on("py-setuptools", type=("build"))
	depends_on("py-bio", type=("build", "run"))
	depends_on("py-cyvcf2", type=("build", "run"))
	depends_on("py-matplotlib", type=("build", "run"))
	depends_on("py-mock", type=("build", "run"))
	depends_on("py-numpy", type=("build", "run"))
	depends_on("py-pandas", type=("build", "run"))
	depends_on("py-seaborn", type=("build", "run"))
	depends_on("py-setuptools", type=("build", "run"))
	depends_on("py-sphinx", type=("build", "run"))
	depends_on("py-scikit-learn", type=("build", "run"))
	depends_on("py-regex", type=("build", "run"))

# {'Bio(>=1.4.0)': ['1.0.0', '1.0.1', '1.0.2', '1.0.4', '1.0.5', '1.0.6'], 'matplotlib(>=3.5.1)': ['1.0.0', '1.0.1', '1.0.2', '1.0.4', '1.0.5', '1.0.6'], 'mock(>=4.0.3)': ['1.0.0', '1.0.1', '1.0.2', '1.0.4', '1.0.5', '1.0.6'], 'numpy(>=1.21.5)': ['1.0.0', '1.0.1', '1.0.2', '1.0.4', '1.0.5', '1.0.6'], 'pandas(>=1.4.2)': ['1.0.0', '1.0.1', '1.0.2', '1.0.4', '1.0.5', '1.0.6'], 'seaborn(>=0.11.2)': ['1.0.0', '1.0.1', '1.0.2', '1.0.4', '1.0.5', '1.0.6'], 'setuptools(>=61.2.0)': ['1.0.0', '1.0.1', '1.0.2', '1.0.4', '1.0.5', '1.0.6'], 'Sphinx(>=4.4.0)': ['1.0.0', '1.0.1', '1.0.2', '1.0.4', '1.0.5', '1.0.6'], 'cyvcf2(>=0.30.18)': ['1.0.4', '1.0.5', '1.0.6'], 'Bio>=1.4.0': ['2.0.8', '2.0.9', '2.1.0'], 'cyvcf2>=0.30.18': ['2.0.8', '2.0.9'], 'matplotlib>=3.5.1': ['2.0.8', '2.0.9', '2.1.0'], 'mock>=4.0.3': ['2.0.8', '2.0.9', '2.1.0'], 'numpy>=1.21.5': ['2.0.8', '2.0.9', '2.1.0'], 'pandas>=1.4.2': ['2.0.8', '2.0.9', '2.1.0'], 'seaborn>=0.11.2': ['2.0.8', '2.0.9', '2.1.0'], 'setuptools>=61.2.0': ['2.0.8', '2.0.9', '2.1.0'], 'Sphinx>=4.4.0': ['2.0.8', '2.0.9', '2.1.0'], 'scikit-learn==1.1.1': ['2.0.8', '2.0.9', '2.1.0'], 'regex>=2023.8.8': ['2.0.8', '2.0.9', '2.1.0'], 'importlib': ['2.0.8', '2.0.9'], 'cyvcf2==0.30.18': ['2.1.0']}