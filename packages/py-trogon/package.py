# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyTrogon(PythonPackage):
	"""Automatically generate a Textual TUI for your Click CLI"""
	
	homepage = "https://github.com/Textualize/trogon"
	pypi = "trogon/trogon-0.6.0-py3-none-any.whl" 

	version("0.6.0", sha256="fb5b6c25acd7a0eaba8d2cd32a57f1d80c26413cea737dad7a4eebcda56060e0", expand=False, url="https://files.pythonhosted.org/packages/97/30/33035d5796a3b8b9624997fec7545e3febd2268c7b48df38a715a95cb5e4/trogon-0.6.0-py3-none-any.whl")
	version("0.5.0", sha256="987d2195c1dd2f93c50e555063a9de57edbc5906ce20ee39081343ff194952c1", expand=False, url="https://files.pythonhosted.org/packages/47/4a/21bb4a3066eacdaa6badbb00e74c75d3ba937712da08d95dd0b318ec46d0/trogon-0.5.0-py3-none-any.whl")
	version("0.4.0", sha256="65fadb5bc25dbd3a2e2f49235fb16735f7b822e24d88b5c68980bb38e1124f99", expand=False, url="https://files.pythonhosted.org/packages/0e/f2/ad49c97be91449ae06061b556371f2d424b8d92c34031e40e9e5bcce7972/trogon-0.4.0-py3-none-any.whl")
	version("0.3.0", sha256="287f22b50cd4cab1f17827ea7180b49e9e1b1a703165e2059bbe1991f3d95115", expand=False, url="https://files.pythonhosted.org/packages/41/c4/4ef341cc25905b983463aa8cb9770d59f305145d3ac068a57b7a2b01789c/trogon-0.3.0-py3-none-any.whl")
	version("0.2.1", sha256="f7c91e226af3f8404d2d2e93ce0838464baea25553efafeb006391f5db458f2c", expand=False, url="https://files.pythonhosted.org/packages/18/b0/6a9cd78ac2f426b1d984150cf9878b93e40a76ed48b253f16125fafc3b84/trogon-0.2.1-py3-none-any.whl")
	version("0.2.0", sha256="ecb0e90a1442a521df8dde596011b9febdc6294c62b4979bc5ad4a46e896ffc4", expand=False, url="https://files.pythonhosted.org/packages/be/f0/32757c7398682722671bb5a57f6ec82fde6adde8712109ba828c352e4f19/trogon-0.2.0-py3-none-any.whl")
	version("0.1.0", sha256="61cd8728fa8f280190c06a60098cea817abaeec49e193406683d7cd8d8eba765", expand=False, url="https://files.pythonhosted.org/packages/32/be/744fad8acae0d22eb1af9000edd19780524f67f448223a777f5624538c41/trogon-0.1.0-py3-none-any.whl")

	depends_on("python@3-8-1:", type=("build", "run"))
	depends_on("py-textual", type=("build", "run"))
	depends_on("py-click", type=("build", "run"))

