# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyDecopatch(PythonPackage):
	"""Create decorators easily in python."""
	
	homepage = "https://github.com/smarie/python-decopatch"
	pypi = "decopatch/decopatch-1.4.9-py2.py3-none-any.whl" 

	version("0.5.0", sha256="b51ad97b323f0af98d771bb8a7e8f4f9c631e5f26162ad2fd2b72bc447a870f7", expand=False, url="https://files.pythonhosted.org/packages/53/36/b0d9e82e4e2b17f0e1615c0cb7394c61c1b4c58da5958964bb380adbe100/decopatch-0.5.0-py3-none-any.whl")
	version("1.0.0", sha256="e3e9b9ce9cc1ca78306ee1f2bd6823659c45e9a5212b71539105388438255fd8", expand=False, url="https://files.pythonhosted.org/packages/cb/3c/807b66488418bd7a2b445981a1023f08f86a553f1fc680f825986eca5189/decopatch-1.0.0-py3-none-any.whl")
	version("1.1.0", sha256="6c05add2c70baa765be80afde5cc69b104063b21003dfe5a3888151980f10e66", expand=False, url="https://files.pythonhosted.org/packages/38/26/b85122f6c5f07a706fcdb63799a002cca9b6d953e2c36674901b808a31b6/decopatch-1.1.0-py3-none-any.whl")
	version("1.1.1", sha256="ee55654d6a9857a15956e07e74a09972578592ccc98185d323be2f4414c4ea9b", expand=False, url="https://files.pythonhosted.org/packages/40/39/c49a413f30c762ec5c9dc2457f97aca4e84be10a322ff678295bfec90150/decopatch-1.1.1-py3-none-any.whl")
	version("1.2.0", sha256="e9db8d2dd2171732e15c6dc170a1400b26e9bab3c633dd6e574f65b04171360b", expand=False, url="https://files.pythonhosted.org/packages/e3/2d/8b68be7e4aef7dfdbf86ee58150532674a8c16731423e71e03898bca5945/decopatch-1.2.0-py3-none-any.whl")
	version("1.2.1", sha256="55f0546f6a445c3726772e838d158dbac1d43012bce82d65b61e4b0f144552c4", expand=False, url="https://files.pythonhosted.org/packages/dc/45/29d07b3fd6df75cb606d503c833d6395bd889ba11939f2107b2726bbc2b9/decopatch-1.2.1-py3-none-any.whl")
	version("1.3.0", sha256="4898dae572bde246af63823e7489d4f1b53f5d9f47b6b7d68260a9849281f9c2", expand=False, url="https://files.pythonhosted.org/packages/cc/a6/7a0a7afbaf16b1f71c73b2ef8f5b514e436404d400e74075e918c533741d/decopatch-1.3.0-py3-none-any.whl")
	version("1.4.0", sha256="a0b0cfa986087e5a45640e1aae393cb2d464d44d87735e7c6886d1e01242c008", expand=False, url="https://files.pythonhosted.org/packages/20/f9/dda5ba412ee583cf0f3fe53b61b414953cc44ba811c2ac9eff7a1cba0e7b/decopatch-1.4.0-py3-none-any.whl")
	version("1.4.1", sha256="2cc63e5e0597e47197e09718ded4bb0b82e807314c0c6ea5b61280ae063a766d", expand=False, url="https://files.pythonhosted.org/packages/cd/6e/5623eda00306a5e14130de1f177ee93d174bedb76b5204832df3640090c9/decopatch-1.4.1-py3-none-any.whl")
	version("1.4.10", sha256="e151f7f93de2b1b3fd3f3272dcc7cefd1a69f68ec1c2d8e288ecd9deb36dc5f7", expand=False, url="https://files.pythonhosted.org/packages/7b/fa/8e4a51e1afda8d4bd73d784bfe4a60cfdeeced9bea419eff5c271180377e/decopatch-1.4.10-py2.py3-none-any.whl")
	version("1.4.2", sha256="97585705d0ad3b78e9f52a06a21362cdc8b390b55884e440481545d7031f2fb4", expand=False, url="https://files.pythonhosted.org/packages/34/37/6781ce755f761846365f02f27168f55bb405da29c5977e97874952058dd0/decopatch-1.4.2-py3-none-any.whl")
	version("1.4.3", sha256="89d4e3ec8c6f86a35583fa17271bea39b7fd604091266dccab5e485012e431c8", expand=False, url="https://files.pythonhosted.org/packages/29/ae/d6aa763a974564177e80ca27dcc7f87a043591662e81170a78afcd695d2d/decopatch-1.4.3-py3-none-any.whl")
	version("1.4.4", sha256="c9db3bfdbb4cd3958560d3caec2954d231e9ae4a9fef9d3512f06833110a6bd5", expand=False, url="https://files.pythonhosted.org/packages/bf/10/02c2260738c3394485992b582fff26461d2e7a3cff70b34091b048df13ac/decopatch-1.4.4-py3-none-any.whl")
	version("1.4.5", sha256="6577b068d8a675bcdc86fb439f20b986518d585526a4d6606a121d78b5840c50", expand=False, url="https://files.pythonhosted.org/packages/80/e0/6ee4f27126fc3578cbced342e8b25c292f6e935889b8929f784170fecde7/decopatch-1.4.5-py3-none-any.whl")
	version("1.4.6", sha256="dddcfab5d6c933dcc2c957f80b4b642bde445a41f4206c4c04b8d76052a881f4", expand=False, url="https://files.pythonhosted.org/packages/c4/f2/ab022f9a93957d71399ead20c5df4ccb537d326caeeae9193d53ba75bda2/decopatch-1.4.6-py3-none-any.whl")
	version("1.4.7", sha256="73e2902d66bb6f9cb85debbd7357b5353acc328d5c2fa4430cbf25c7769bdf0f", expand=False, url="https://files.pythonhosted.org/packages/68/cf/5f2e4fade22781703ce17188d5277d8cb4981bcb3f9d3736fbdcf48e10e7/decopatch-1.4.7-py3-none-any.whl")
	version("1.4.8", sha256="29a74d5d753423b188d5b537532da4f4b88e33ddccb95a8a20a5eff5b13265d4", expand=False, url="https://files.pythonhosted.org/packages/9b/17/c48e8989ada9be380bbf7f2911aefa0f56d87a7ddc9b48a536284e85f11d/decopatch-1.4.8-py2.py3-none-any.whl")
	version("1.4.9", sha256="cd9a49f749c26ea8e5fc567b0ccc04f61fb83ebd6eea0834e426f327399a7757", expand=False, url="https://files.pythonhosted.org/packages/ef/7a/b3ea765fbd6b84b9834df7c7b99e4219b063ca66791257fa788a8f29615b/decopatch-1.4.9-py2.py3-none-any.whl")

	depends_on("py-setuptools", type=("build"))
	depends_on("py-makefun", type=("build", "run"))
	depends_on("py-funcsigs", type=("build", "run"))

# {'makefun': ['0.5.0', '1.0.0'], 'funcsigs;python_version<"3.3"': ['0.5.0', '1.0.0', '1.1.0', '1.1.1', '1.2.0', '1.2.1', '1.3.0', '1.4.0', '1.4.1', '1.4.10', '1.4.2', '1.4.3', '1.4.4', '1.4.5', '1.4.6', '1.4.7', '1.4.8', '1.4.9'], 'enum34;python_version<"3.4"': ['0.5.0', '1.0.0', '1.1.0', '1.1.1', '1.2.0', '1.2.1', '1.3.0', '1.4.0', '1.4.1', '1.4.10', '1.4.2', '1.4.3', '1.4.4', '1.4.5', '1.4.6', '1.4.7', '1.4.8', '1.4.9'], 'makefun(>=1.3.0)': ['1.1.0', '1.1.1'], 'makefun(>=1.4.0)': ['1.2.0', '1.2.1', '1.3.0'], 'makefun(>=1.5.0)': ['1.4.0', '1.4.1', '1.4.10', '1.4.2', '1.4.3', '1.4.4', '1.4.5', '1.4.6', '1.4.7', '1.4.8', '1.4.9']}