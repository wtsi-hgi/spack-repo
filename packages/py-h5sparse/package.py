# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyH5sparse(PythonPackage):
	"""Scipy sparse matrix in HDF5."""
	
	homepage = "https://github.com/appier/h5sparse"
	pypi = "h5sparse/h5sparse-0.1.0-py2.py3-none-any.whl" 

	version("0.0.1", sha256="e2113138903239dda69f22a99f7890b7dfa26024a9a72141f3ecd505e9672eae", expand=False, url="https://files.pythonhosted.org/packages/5b/34/5bc3738623850b9dffc008010bd8400a013d8e0cc2b54cbdfc4b3c33af93/h5sparse-0.0.1-py2.py3-none-any.whl")
	version("0.0.2", sha256="4480d21cab952b47823322558246d20c90702b47c53c53bae46a0631adffd2fe", expand=False, url="https://files.pythonhosted.org/packages/ba/9a/5f58f4c536ac4e1175d5638a8e89fa25b6706606346f49f8df0c03d93078/h5sparse-0.0.2-py2.py3-none-any.whl")
	version("0.0.3", sha256="f2df32a867369ba1bd7a28b866fb9d97bf769e2bba1d149cfc8735345675fd6f", expand=False, url="https://files.pythonhosted.org/packages/d8/37/1e1253987b4892e63511b4e867c8248ae3d6476d3859f26ee152bd21f732/h5sparse-0.0.3-py2.py3-none-any.whl")
	version("0.0.4", sha256="27e40f3d104874b878c60929403ae2d15a89d3506e580978aece4aa1a9e62dc3", expand=False, url="https://files.pythonhosted.org/packages/fb/5c/28fac0c987f53f7bbad1f13e98f470258c1cf7ff401a4b647d5c1218c8e4/h5sparse-0.0.4-py2.py3-none-any.whl")
	version("0.0.5", sha256="4b0a7b0f91f8a43a2f1b4ea1c62dca02b5634bda5e81a38f894518bf4b29d8d9", expand=False, url="https://files.pythonhosted.org/packages/fb/44/44dc2f8e09eb179b77f47b354bba186ba2db9119b0cbf39067b0a92adcc7/h5sparse-0.0.5-py2.py3-none-any.whl")
	version("0.1.0", sha256="03595909c9fd4e895c4b3f12ca7a1e7f95a5cb3610f07d862d7f59612e0302fa", expand=False, url="https://files.pythonhosted.org/packages/40/ee/8be7e1ba3844dc45e99e648d22fe214c8391c9e26245942221fea72a7e30/h5sparse-0.1.0-py2.py3-none-any.whl")

	depends_on("py-six", type=("build", "run"))
	depends_on("py-scipy", type=("build", "run"))
	depends_on("py-numpy", type=("build", "run"))
	depends_on("py-h5py", type=("build", "run"))

# {'h5py': ['0.0.1', '0.0.2', '0.0.3', '0.0.4', '0.0.5', '0.1.0'], 'numpy': ['0.0.1', '0.0.2', '0.0.3', '0.0.4', '0.0.5', '0.1.0'], 'scipy': ['0.0.1', '0.0.2', '0.0.3', '0.0.4', '0.0.5', '0.1.0'], 'six': ['0.0.3', '0.0.4', '0.0.5', '0.1.0']}