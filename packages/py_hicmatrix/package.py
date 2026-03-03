# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyHicmatrix(PythonPackage):
	"""Helper package which implements HiCMatrix class for HiCExplorer, pyGenomeTracks and scHiCExplorer."""
	
	homepage = "https://github.com/deeptools/HiCMatrix"
	pypi = "HiCMatrix/HiCMatrix-7-py3-none-any.whl" 

	version("10", sha256="aff921ce67ce0315edfafa0385777ee3eddb8ab5a38c3ffb165d6308b6201d2b", expand=False, url="https://files.pythonhosted.org/packages/bb/f8/362fe53953cbdaea5d043dab5d888f9b9928ff68b6810d86b81737cb0f25/HiCMatrix-10-py2-none-any.whl")
	version("11", sha256="bf472cd844615a90281b1885522bbf9f84d4bc904791020511a64d4ddb061ad8", expand=False, url="https://files.pythonhosted.org/packages/46/4b/0618c840e63f386275d58ce3fb40a1bc2291abb65066f696ed45a43420c9/HiCMatrix-11-py3-none-any.whl")
	version("12", sha256="8c64ddf44033dcb440f522b6078ce8f5dd93bbc5073c10aa130a3232b2cfb200", expand=False, url="https://files.pythonhosted.org/packages/40/92/259704bbd3d1beb8c2429ad4982fd53a5e5fb38037feeec8c8821e67cdbc/HiCMatrix-12-py3-none-any.whl")
	version("13", sha256="88d4e43dddf87be7d9e0f76de799b018068f412f2d20509a16a7f444f5612cd1", expand=False, url="https://files.pythonhosted.org/packages/0d/f5/e2536a490bf6da6a5c9c7ddfab9f1bb674436beca23c1c1e1d701602207f/HiCMatrix-13-py3-none-any.whl")
	version("15", sha256="634967ad72f9cbb27dfe35c7f14a6210309f6de3c22735a56c8c554cc5a5c484", expand=False, url="https://files.pythonhosted.org/packages/16/d9/65b4da937e747ca21ed7faf6959fbc9d8373de6b467659101aabf2080b61/HiCMatrix-15-py3-none-any.whl")
	version("17.1", sha256="717786239f2a6a3313829289a5c367255fd6875d30f0f11c511765c4fb279036", expand=False, url="https://files.pythonhosted.org/packages/5d/88/5d7a4841c8b4fb2791a55562dbf50f48d66165c141c8daa9bca9e6e141c0/HiCMatrix-17.1-py3-none-any.whl")
	version("17.2", sha256="6e926c3773fc0e6ac6ea0ffd9a800664c77849052de214fc2c387da07571d61a", expand=False, url="https://files.pythonhosted.org/packages/82/4d/1fcf74ad06b114f3ae4a528f582bba38330cb71a5c4afe58e4752a8a7dd0/HiCMatrix-17.2-py3-none-any.whl")
	version("5", sha256="7387dd6233db1fe521afb376bfd097701e6e4b7a28b510c1af8c92ce8d7c62b7", expand=False, url="https://files.pythonhosted.org/packages/c5/f7/63896fd185f2ba9ded78799f436ccda767bb96c90a8c4ee1b663ebf621e8/HiCMatrix-5-py3-none-any.whl")
	version("7", sha256="452c30e78c3658b68ffab798d3e3b438ae14972ed4a56f0744c96fdf28132f6f", expand=False, url="https://files.pythonhosted.org/packages/6f/e2/43a182d7e06a763196a271fa88de9053438fe2dbfd44b53e185b879f6286/HiCMatrix-7-py3-none-any.whl")

	depends_on("python@3.7:", type=("build", "run"))
	depends_on("py-intervaltree", type=("build", "run"))
	depends_on("py-cooler", type=("build", "run"))
	depends_on("py-future", type=("build", "run"))
	depends_on("py-pandas", type=("build", "run"))
	depends_on("py-tables", type=("build", "run"))
	depends_on("py-scipy", type=("build", "run"))
	depends_on("py-numpy", type=("build", "run"))

# {'numpy(>=1.16.*)': ['10', '11', '12', '13', '15'], 'scipy(>=1.2.*)': ['10', '11', '12', '13', '15'], 'tables(>=3.5.*)': ['10', '11', '12', '13', '15'], 'pandas(>=0.24.*)': ['10', '11'], 'future(>=0.17.*)': ['10'], 'cooler(==0.8.5)': ['10', '11', '12'], 'intervaltree(==3.0.*)': ['10', '11', '12'], 'pandas(>=0.25.*)': ['12', '13', '15'], 'cooler(>=0.8.*)': ['13'], 'intervaltree(>=3.0.*)': ['13', '15'], 'cooler(>=0.8.9)': ['15'], 'numpy>=1.20': ['17.1', '17.2'], 'scipy>=1.2': ['17.1', '17.2'], 'tables>=3.5': ['17.1', '17.2'], 'pandas>=0.25': ['17.1', '17.2'], 'cooler>=0.8.9': ['17.1', '17.2'], 'intervaltree>=3.0': ['17.1', '17.2'], 'importlib-metadata;python_version<"3.8"': ['17.2'], 'numpy(>=1.13.*)': ['5', '7'], 'scipy(>=1.1.*)': ['5', '7'], 'tables(>=3.4.*)': ['5', '7'], 'pandas(>=0.23.*)': ['5', '7'], 'future(>=0.16.*)': ['5', '7'], 'cooler(==0.7.11)': ['5'], 'intervaltree(==2.1.*)': ['5', '7'], 'cooler(==0.8.2)': ['7']}