# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyIpydatawidgets(PythonPackage):
	"""A set of widgets to help facilitate reuse of large datasets across widgets"""
	
	homepage = "https://github.com/vidartf/ipydatawidgets"
	pypi = "ipydatawidgets/ipydatawidgets-4.3.5-py2.py3-none-any.whl" 

	version("1.0.1", sha256="873e0c3ee72e7dd9e7a8609df6d9986262d2d4b41e652946f43693c8e8d6f2ef", expand=False, url="https://files.pythonhosted.org/packages/e8/e2/c9627c974cea1282fd2fb200759ca81e33753e106c5cea0f834b2db79ebd/ipydatawidgets-1.0.1-py2.py3-none-any.whl")
	version("1.0.2", sha256="3aa8261fa670057e575ce3a449411195aac8994056fbbe87b30b59f1fd655be8", expand=False, url="https://files.pythonhosted.org/packages/71/36/39ddc9ecb42115ae39b9edceed1650c9206643a6cbd2ff20371290f82a7e/ipydatawidgets-1.0.2-py2.py3-none-any.whl")
	version("1.1.0", sha256="cb1c85bbf1171dedd738f48f07f1c4418fb848147c342f1353b1ea960e7039fd", expand=False, url="https://files.pythonhosted.org/packages/32/87/8e9ac386b7433bb61a7af803f375615cf3babe83fef2b97b597eab93eb40/ipydatawidgets-1.1.0-py2.py3-none-any.whl")
	version("1.1.1", sha256="9c96d0b908da059fe188185ed0ac3301067cfd3d738c14e06ccb1e7754d43ab0", expand=False, url="https://files.pythonhosted.org/packages/2e/d0/0c131dfeb7a5d1031f4f23a01c79d60c87753b4861e31475935bc63483dc/ipydatawidgets-1.1.1-py2.py3-none-any.whl")
	version("1.1.2", sha256="a5e42d54b0949f1e80e580938582e9bbb3ff05d8d66f229727d473aa17dae05b", expand=False, url="https://files.pythonhosted.org/packages/63/0d/f9af2373846862d8f1d35d6ecf0916ed8e2ac48c1ec7f6ce5611c66c37e2/ipydatawidgets-1.1.2-py2.py3-none-any.whl")
	version("1.2.0", sha256="7e5fb247a27b858804dd2d1e788b78cc69a2ae25dce7fa3ead5d3338b933a957", expand=False, url="https://files.pythonhosted.org/packages/c3/ca/cf8adb7444a18ddea30f22c356b5751bbc4655a5cea05b3eb2a283f1d4a3/ipydatawidgets-1.2.0-py2.py3-none-any.whl")
	version("1.2.1", sha256="b87638f1cc3f9f035bddb75cd3a97e26de0786bfb3e9c914f836cafd87fafece", expand=False, url="https://files.pythonhosted.org/packages/4d/1f/03c5aab514dc27e1f6f04e837bd17e95310788bf35ba2eb975d4ce79082e/ipydatawidgets-1.2.1-py2.py3-none-any.whl")
	version("1.2.2", sha256="74b0340da04791b97be119a7c5723bde811b7db7b870ed7ac066d29bf22ed729", expand=False, url="https://files.pythonhosted.org/packages/6e/85/8a4bb9f654b41538dcfa78a149f010c3aa39b7af087341aa9574a881bfae/ipydatawidgets-1.2.2-py2.py3-none-any.whl")
	version("2.0.0", sha256="e39932273eca7252b1f52928ba9dac59d1aeb6b5c5dae4b10c45cdfd6c935ed1", expand=False, url="https://files.pythonhosted.org/packages/de/6d/cfec35779a8ecfe6bd084addcaae7321cdf1f34aa43392114bfc2da36e54/ipydatawidgets-2.0.0-py2.py3-none-any.whl")
	version("3.0.0", sha256="76b9d899a529cd34fe549a68e41a6cee84dd96aa05180f25019e67b1de19e848", expand=False, url="https://files.pythonhosted.org/packages/0d/1c/8c8d08a339d82e6f6ae59c0a2b05b1d415f12ae8cdfbe802376a1d5f50ed/ipydatawidgets-3.0.0-py2.py3-none-any.whl")
	version("3.1.0", sha256="376b30b4e94a720dd755573631190474eeaff6594afa71e2195b3a427aa5a630", expand=False, url="https://files.pythonhosted.org/packages/f9/25/0f9a2663587bee7f3c26317f16d891e048a6f94ea785911474d5873013c4/ipydatawidgets-3.1.0-py2.py3-none-any.whl")
	version("3.2.0", sha256="cb22dfd12d3771785d9fa318ad76ac7d0eee2d8c31e496f13a279efbbecf04fa", expand=False, url="https://files.pythonhosted.org/packages/d3/cf/993122ee6f676379b29c50721f9b79ba027974ac94c1ebff7b79d33e1ee1/ipydatawidgets-3.2.0-py2.py3-none-any.whl")
	version("4.0.0", sha256="229d2c08d86150522c3f6351a4102c3285a585a067073b96824378eaf9ce261c", expand=False, url="https://files.pythonhosted.org/packages/2c/9e/16c3cbc63862b36c0b18aa0e1d1dd6a65496d4f8a91a57a728d19bdb74b1/ipydatawidgets-4.0.0-py2.py3-none-any.whl")
	version("4.0.1", sha256="d563627a5e6542f258d71849818708a57fd258bf1fddaea64c9ed42bf6dcdf96", expand=False, url="https://files.pythonhosted.org/packages/3d/62/eb221e1efaebf42af438c109088fbeea00561e5567a202fc8425d7b9c34d/ipydatawidgets-4.0.1-py2.py3-none-any.whl")
	version("4.1.0", sha256="39fb61efd5486cfc9905d262cc12bdeebd8e9eba9df3f3108fa19d53aa41d974", expand=False, url="https://files.pythonhosted.org/packages/59/6f/13714dcb834d0b35cec3eb1d4f2723d36be44e71283df51c4326179c3414/ipydatawidgets-4.1.0-py2.py3-none-any.whl")
	version("4.2.0", sha256="ace4d2aa68c0667290873bbc8a5a2948afe40c80f7c93c7c2b19d38c2e91c08f", expand=False, url="https://files.pythonhosted.org/packages/5d/58/9ec5a0e1653ffc762674370c4ebbcb5132b9c0691942a8c9a805a8b80b5e/ipydatawidgets-4.2.0-py2.py3-none-any.whl")
	version("4.3.1", sha256="77f18736b842729c0d6876679eb5ce53db1212d133b9136753b0f0f77a41dc28", expand=False, url="https://files.pythonhosted.org/packages/d5/b0/cb6abeca80cfc6ec1a3a42d6e2d43d9a3610725f0857033c6d170c53d6d0/ipydatawidgets-4.3.1-py2.py3-none-any.whl")
	version("4.3.1.post1", sha256="645ce22334a8c1e97637c7e8c40548ad9d7a5f4097748cf22745dad09cab7c49", expand=False, url="https://files.pythonhosted.org/packages/84/e1/ff6c118e5d6fef09763159009a3952f4ac1b248bae2a571abc2b2e2faab3/ipydatawidgets-4.3.1.post1-py2.py3-none-any.whl")
	version("4.3.2", sha256="c1d8e479f3adafba42378fe39126ddc14293ccb90341eeb2f6c1f568aa019c64", expand=False, url="https://files.pythonhosted.org/packages/29/75/b654fe4a12e45313642119ed09f90a52af7220bc97e016e87cc7270b9167/ipydatawidgets-4.3.2-py2.py3-none-any.whl")
	version("4.3.3", sha256="8e2a34232b927c2a06bcfe7ea734f39b38cf7e4fd917e78484cae671b2779e6e", expand=False, url="https://files.pythonhosted.org/packages/ac/32/bb39bd53918647865894624b496b3294411b1ea1da702f003a224de20d90/ipydatawidgets-4.3.3-py2.py3-none-any.whl")
	version("4.3.4", sha256="c9c0cbca4b48213988a2f05b84f039be7647fbb895be1d82c7c53f2f35087c8e", expand=False, url="https://files.pythonhosted.org/packages/9a/e6/728546548ff3c64fd64224db57553ccd538532b3d8f704c453477a4f03d8/ipydatawidgets-4.3.4-py2.py3-none-any.whl")
	version("4.3.5", sha256="d590cdb7c364f2f6ab346f20b9d2dd661d27a834ef7845bc9d7113118f05ec87", expand=False, url="https://files.pythonhosted.org/packages/f1/5b/e63c877c4c94382b66de5045e08ec8cd960e8a4d22f0d62a4dfb1f9e5ac6/ipydatawidgets-4.3.5-py2.py3-none-any.whl")

	depends_on("python@3.7:", type=("build", "run"))
	depends_on("py-traittypes", type=("build", "run"))
	depends_on("py-numpy", type=("build", "run"))
	depends_on("py-ipywidgets", type=("build", "run"))
