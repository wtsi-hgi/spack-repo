# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPybgen(PythonPackage):
	"""Python module to read BGEN files."""
	
	homepage = "https://github.com/lemieuxl/pybgen"
	pypi = "pybgen/pybgen-0.7.1-py2.py3-none-any.whl" 

	version("0.1.0", sha256="fc671a1720c830cb92f7dbe249d046bdaaa840ac237fc858cc51036886fffeba", expand=False, url="https://files.pythonhosted.org/packages/c2/d4/37c75c430b57b90a0c135e15dc7f0972141917533ad5967a497d481609ba/pybgen-0.1.0-py2.py3-none-any.whl")
	version("0.2.0", sha256="3f111f2437a69024040aa8a436b84d8b94186e5ae80d3d33549fcf437a126aad", expand=False, url="https://files.pythonhosted.org/packages/04/c0/ddc7cacc152b6c5efedb8ab5037519ff60ec8e8ceeaabd623c125e8271cc/pybgen-0.2.0-py2.py3-none-any.whl")
	version("0.3.0", sha256="958f004f2463c2329d8452673ff8efffb2947df7e2ba90e70e87eda8dbe353ad", expand=False, url="https://files.pythonhosted.org/packages/5f/f9/803bfbd0b27ac519eba0866d6d6fabb68b3f4f9bd6c818e882b32cd3a939/pybgen-0.3.0-py2.py3-none-any.whl")
	version("0.3.1", sha256="055b9736ea782f0114c440160e649b735e12a133f8a831297c69d00e668f63cd", expand=False, url="https://files.pythonhosted.org/packages/0f/4c/b80a2c26c468fb06a47c90d81dec94116d4abf7482e242052a49e8b3deaf/pybgen-0.3.1-py2.py3-none-any.whl")
	version("0.4.0", sha256="b2d822eebb538608ae9d0f16ae4999e78b4c3bde61e286a7fc5ee5afa7e61273", expand=False, url="https://files.pythonhosted.org/packages/2c/e9/6f976078c3ad8d75bf9026d4943f48d08b18c44c3178680ee069fbd00ab9/pybgen-0.4.0-py2.py3-none-any.whl")
	version("0.4.1", sha256="7f46275cd42fcc61170ca75c6b914d4ff199eb1c14f20c6de334b5ea825d4bda", expand=False, url="https://files.pythonhosted.org/packages/09/59/3a01e7a79eb891d0a202c8398bf6270896ce7bb8f79f00df19492e4f2276/pybgen-0.4.1-py2.py3-none-any.whl")
	version("0.4.2", sha256="e2b07622eeeeb4e7af9ad02c9a79ce45908834e913cc2ebbe06776dff30cba69", expand=False, url="https://files.pythonhosted.org/packages/66/0f/71a0282c1958eb60fc848fdbf2420dcd4059a4be03705b26d091bc1d717f/pybgen-0.4.2-py2.py3-none-any.whl")
	version("0.5.0", sha256="384fb705f7d64f510b6934f7f1a7186dff20da3a8c7e0f6bf980fa3d56f3779c", expand=False, url="https://files.pythonhosted.org/packages/08/d0/e4c13cd8775bd3a554ab908e7e9efb693a874c139f528c23aaebad5e81b0/pybgen-0.5.0-py2.py3-none-any.whl")
	version("0.6.0", sha256="92788bddfe7d3eb665f1a026d3a32d74efa743342428b03d577a888c3399a0eb", expand=False, url="https://files.pythonhosted.org/packages/c0/24/d8e4512f171285d745fd69814368d7995b06af5e418917d473c9c39632c3/pybgen-0.6.0-py2.py3-none-any.whl")
	version("0.7.0", sha256="2b20045052883bf4ccf693b1f0b5113a932a6091b76a295e26fb2608a6bd6dba", expand=False, url="https://files.pythonhosted.org/packages/3e/86/e8be146b87e02a826442fb2164d417d22c189c098b1d7eff8045e5cdb497/pybgen-0.7.0-py2.py3-none-any.whl")
	version("0.7.1", sha256="78fd1e8bb55a7fcd9b576008f82b1d971d114883085c0041d2d2f679ec8e5467", expand=False, url="https://files.pythonhosted.org/packages/20/35/892168d60150e1f28b9b42c82edb54bb32673706d07f42fab357189e9903/pybgen-0.7.1-py2.py3-none-any.whl")

	depends_on("py-setuptools", type=("build", "run"))
	depends_on("py-six", type=("build", "run"))
	depends_on("py-numpy", type=("build", "run"))

# {'numpy(>=1.13.0)': ['0.1.0', '0.2.0', '0.3.0'], 'setuptools(>=27.0)': ['0.1.0', '0.2.0', '0.3.0', '0.3.1', '0.4.0', '0.4.1', '0.4.2', '0.5.0', '0.6.0', '0.7.0', '0.7.1'], 'six(>=1.10.0)': ['0.1.0', '0.2.0', '0.3.0', '0.3.1', '0.4.0', '0.4.1', '0.4.2', '0.5.0', '0.6.0', '0.7.0', '0.7.1'], 'numpy(>=1.11.0)': ['0.3.1', '0.4.0', '0.4.1'], 'numpy(>=1.12.0)': ['0.4.2', '0.5.0', '0.6.0', '0.7.0', '0.7.1']}