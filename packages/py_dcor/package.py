# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyDcor(PythonPackage):
	"""dcor: distance correlation and energy statistics in Python."""
	
	homepage = "https://github.com/vnmabus/dcor"
	pypi = "dcor/dcor-0.6-py3-none-any.whl" 

	version("0.1", sha256="af262a35c356bf07d85d8eb725214150f99fd95afbab2c5ffc8317d63c6826a5", expand=False, url="https://files.pythonhosted.org/packages/bf/db/c32e64c0db99da3dbf3ac174634245c03a40c2eeda47f7192cb61bc49733/dcor-0.1-py2.py3-none-any.whl")
	version("0.1.1", sha256="a7020456195011bff83b2cec364f6aecc77e1305de65f866c26b5ad4d9df5a3a", expand=False, url="https://files.pythonhosted.org/packages/77/f9/7d69ef8e2cff3d48915bd8b382333e1fccff2d365b18f8cf01a9311cfb4e/dcor-0.1.1-py2.py3-none-any.whl")
	version("0.1.2", sha256="c3e7c0147caf70a878eec74b76bcf1a82b9bcbf3875f6c03fd02fab0d3057a77", expand=False, url="https://files.pythonhosted.org/packages/39/96/1a1466d7b08ceabbd5ce88f6d91ea136f9ed72076407c2319773db091628/dcor-0.1.2-py2.py3-none-any.whl")
	version("0.1.3", sha256="ca1240091354303b72054c3b5a67ba406e032305e4f4a0b35c42c03841e94736", expand=False, url="https://files.pythonhosted.org/packages/a0/e5/f25c029a191d24f79c55f413162a73ef8487e2c4c1999033d834975a8fe0/dcor-0.1.3-py2.py3-none-any.whl")
	version("0.1.4", sha256="f512c406ca49caaba2e620253c3b2266ac54af152766ac362bd2ea992e396517", expand=False, url="https://files.pythonhosted.org/packages/e7/26/eaf5105483987df6f8b120f1acfef1e61a4fdd4faf80b227fb4150acf330/dcor-0.1.4-py2.py3-none-any.whl")
	version("0.1.5", sha256="b385d410b2ce153554e3bcebac5114dc516de1ba9fd9c95fa7201b806948cd4b", expand=False, url="https://files.pythonhosted.org/packages/6a/54/b0df066a28128073d9eb2d6a339304476aeb52c30e3df09a95945165c2e4/dcor-0.1.5-py2.py3-none-any.whl")
	version("0.2", sha256="655e2852d36fcd2d4b64db970d0fa013a96c14acd089939eb5fdb622fe3287ea", expand=False, url="https://files.pythonhosted.org/packages/14/27/4cf297cdfb678b42693a170acebf9a493f7e30479991ca0c783d62d5a3f0/dcor-0.2-py2.py3-none-any.whl")
	version("0.3", sha256="4f85f3176e648dc531e8fc1608ec6b3d3f68bfb427b7bb792604638577ffa87b", expand=False, url="https://files.pythonhosted.org/packages/46/7d/11fda8c9186dc67edd862daf209144a5d372035b5b9449f314c6f1990dbc/dcor-0.3-py2.py3-none-any.whl")
	version("0.4", sha256="309550e7c83258e6a376d66a4627444325da75e0d54a6f4932c518588c4ddf37", expand=False, url="https://files.pythonhosted.org/packages/e4/c7/0e9858d2137655e54c4ca6815ddf16fcdd47f1916ff80b57a3b6665f3e36/dcor-0.4-py2.py3-none-any.whl")
	version("0.5", sha256="f20c704459bf42a3ab64d28fa956732040b32e54614e740cd3c076b6c5efd19e", expand=False, url="https://files.pythonhosted.org/packages/a9/59/ea5963dd250dca4d84a44f581041f9877dce2769fb68d3ca0e379957033d/dcor-0.5-py2.py3-none-any.whl")
	version("0.5.1", sha256="5979fe1a18d0e52613ccb3a6299b879f7a4ebbb32db47a3ff04686b2a3adc95b", expand=False, url="https://files.pythonhosted.org/packages/ac/e0/5f8f1feaf4b94118423b4c837cfd5504863c19f95e76241ddb655e3592d0/dcor-0.5.1-py2.py3-none-any.whl")
	version("0.5.2", sha256="747999f47323b9c07c1ad1210235a25486d0517a997452add74016df7e2cf0ec", expand=False, url="https://files.pythonhosted.org/packages/91/43/2e2a4acb8fcac32b2702cc0a17b80d66b7453994744d226640d3a349c735/dcor-0.5.2-py2.py3-none-any.whl")
	version("0.5.3", sha256="88534cacca9ce57b186d989a3ea312bb3d304747f9db576019a86d6691f31c23", expand=False, url="https://files.pythonhosted.org/packages/14/15/f49cbce4fc43455b387ba1512c7242db4e9181b1c1aaa6c8eb8412226c16/dcor-0.5.3-py2.py3-none-any.whl")
	version("0.5.5", sha256="a66e29e7c36293a65861468d69346515777c1774dd7f1ecffd3db9eeffe86b89", expand=False, url="https://files.pythonhosted.org/packages/35/1b/9d699c863b186068d8b840229171e08a17bb8d1b941a41752b3c46c7a099/dcor-0.5.5-py3-none-any.whl")
	version("0.5.6", sha256="8dbf20cb4b84b9fce37fd159043ae3a6a43b37de34ee627fedfe2833c29ab479", expand=False, url="https://files.pythonhosted.org/packages/f0/a8/3cba4873795ee63d278d1e463e4c12d6ac65c2b33391e601be0a47cfa7dd/dcor-0.5.6-py3-none-any.whl")
	version("0.5.7", sha256="6a459da3c6f5441ccc1c460376d8c96aade8e48d46b395aaf35337768b16b7aa", expand=False, url="https://files.pythonhosted.org/packages/c9/92/458697bf3a46fb1c593d3f1cdb2e5d3b5b0da68e244c856a71452ea878df/dcor-0.5.7-py3-none-any.whl")
	version("0.6", sha256="de306fc666668188749730fc803fc1d4d804d9886c92b622ba57b434fed395a2", expand=False, url="https://files.pythonhosted.org/packages/45/f3/49770c523067d2179a600f236ea6d55f0a02909a424d055dbc50e04c4860/dcor-0.6-py3-none-any.whl")

	depends_on("python@3.8:", type=("build", "run"))
	depends_on("py-numpy", type=("build", "run"))
	depends_on("py-scipy", type=("build", "run"))
	depends_on("py-joblib", type=("build", "run"))
	depends_on("py-numba", type=("build", "run"))

	@run_after("install")
	def install_test(self):
		self.spec["python"].command("-c", "import dcor")
