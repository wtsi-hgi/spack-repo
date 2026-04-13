# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPdiff(PythonPackage):
	"""Pretty side-by-side diff"""
	
	homepage = "https://github.com/nkouevda/pdiff"
	pypi = "pdiff/pdiff-1.1.5-py3-none-any.whl" 

	version("1.1.5", sha256="9dc2327b96548c6fefb94d5bc4e689eff5460f36debabb829bb8f68ead98bcf5", expand=False, url="https://files.pythonhosted.org/packages/6e/71/c44139446f1d58dab87c9d588229b6973e6abab987d85902ab8b5522c815/pdiff-1.1.5-py3-none-any.whl")
	version("1.1.4", sha256="ff50f19caffb7415c4244363233e019669b35b5ec43bd5f0f84f6837ab1068a4", expand=False, url="https://files.pythonhosted.org/packages/f3/52/74ae783736e30a36db773372a97a9c2c93144c4a83bc43eef5df93572aee/pdiff-1.1.4-py3-none-any.whl")
	version("1.1.3", sha256="256b2043de086e63e0e92de3e48b8dd9c28fee4bc28cc4bf898068104f0f60cf", expand=False, url="https://files.pythonhosted.org/packages/95/1a/5fe42737025ad3cdf1601902ad8a1fbc0b531de21c39bc5ecdb9f1dd86f5/pdiff-1.1.3-py3-none-any.whl")
	version("1.1.2", sha256="3634efe2d10b43753d02c4d5727b38e2ddaf81398367669d289989d9d5c527e5", expand=False, url="https://files.pythonhosted.org/packages/73/dd/344b1235433625109d34ced2f7625931eaf7241eee790925d9dbe0ee9e83/pdiff-1.1.2-py3-none-any.whl")
	version("1.1.1", sha256="94cd6a42cd33c3961d6a60bf484616450bf7a4254f7702b3a33f0135bbb42b2e", expand=False, url="https://files.pythonhosted.org/packages/3c/51/c9d729491cd0838cdc89610d1d43f5dae85c079a80e39e23380c73953321/pdiff-1.1.1-py3-none-any.whl")
	version("1.1.0", sha256="262ea927515da585894c4691495b467339cffbb9097292dde056ffeac8f3421f", expand=False, url="https://files.pythonhosted.org/packages/4e/72/a73e70d3d1c5d8ce18afa523f6a493e7402d037a4fc55d7f98b792843dad/pdiff-1.1.0-py3-none-any.whl")
	version("1.0.8", sha256="0ce1a21108751ca22160612fc523868d84f56138323a01ab2953b7f59869430f", expand=False, url="https://files.pythonhosted.org/packages/3b/e6/2fe361d77cda140930c55b6f0e5f9d6c8602099a1e392170d811fb456df1/pdiff-1.0.8-py3-none-any.whl")
	version("1.0.7", sha256="943816547b71d5e56f16e23cf5eccd78d7f24e0cf6949cc67000dfdf5e303709", expand=False, url="https://files.pythonhosted.org/packages/40/10/408433eca20ea22c864a778f6d3866d8b2302860216c6ac8ad0bcb6f57cd/pdiff-1.0.7-py3-none-any.whl")
	version("1.0.6", sha256="dfc4f8efc88444f227097fc3dcbae33298de484a2892839a5ca667f26ed4fb1d", expand=False, url="https://files.pythonhosted.org/packages/da/46/a5e59ef70735d5684c46fdd20f05d2703df19ef4c10ff7c2f334061f619f/pdiff-1.0.6-py3-none-any.whl")
	version("1.0.5", sha256="a8ef3a8fa54e7a830c839bd1b98d965f901575a133f845234b2d515a13cefce8", expand=False, url="https://files.pythonhosted.org/packages/fd/20/c7f6a32e097824d2320add601d38146b61ac2605e13042390798a04ae85d/pdiff-1.0.5-py2.py3-none-any.whl")
	version("1.0.4", sha256="c0f3d71de4d5c34578f93e66276f3f0b5028675111d2d208ddcca7402c29bd20", expand=False, url="https://files.pythonhosted.org/packages/7e/53/dafc98ea8594ac212fa550ee47361fd2ae19264f1b80c6ba216c160f6562/pdiff-1.0.4-py2.py3-none-any.whl")
	version("1.0.3", sha256="1a7a2c4af7f13d88fa028d0e9ff6df922f8f5e8aef14a22a396feb732db9c7ad", expand=False, url="https://files.pythonhosted.org/packages/9e/21/ff2466290c0a2b0ce868132c2c3e917ecc164a73bda704ea574aa0965bf9/pdiff-1.0.3-py2.py3-none-any.whl")
	version("1.0.2", sha256="1c664a84a268528c665277a9402639bd27c37af03ffb611707c1f812e806bc50", expand=False, url="https://files.pythonhosted.org/packages/5b/b5/bd3729a36dfc3634a210babe285e94d2097a968cde65e6d03bfade0f6008/pdiff-1.0.2-py2.py3-none-any.whl")
	version("1.0.1", sha256="053de2e67e6b57c4aa6b9e3c29b4feb957f75bf537ab81653db62fb944704ccc", expand=False, url="https://files.pythonhosted.org/packages/1c/5d/114359ed5f0798274698cef89c18fae74b8357f0cee7cab8147da9bd1ea7/pdiff-1.0.1-py2.py3-none-any.whl")
	version("1.0.0", sha256="bf2f73bb48bda6375c8b9ead264f34713e0f34dc59a6d2a76843efcf04b8e709", expand=False, url="https://files.pythonhosted.org/packages/a4/85/654862ec8522847ec622e597af39c7274de319960dcebeafed8674b147a4/pdiff-1.0.0-py2.py3-none-any.whl")

	depends_on("py-colorama", type=("build", "run"))
