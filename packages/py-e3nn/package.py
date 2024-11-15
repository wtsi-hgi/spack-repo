# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyE3nn(PythonPackage):
	"""Equivariant convolutional neural networks for the group E(3) of 3 dimensional rotations, translations, and mirrors."""
	
	homepage = "https://e3nn.org"
	pypi = "e3nn/e3nn-0.5.4-py3-none-any.whl" 

	version("0.0.0", sha256="0a84b301f065ad371d608ce71d7ffde8bfdee7df9d3d3a532fa858f03b8d7e93", expand=False, url="https://files.pythonhosted.org/packages/ed/34/41ec81a75d116c5ccd327a8dade0f3fe114b78c6841001fcf030cd1b901f/e3nn-0.0.0-py3-none-any.whl")
	version("0.0.2", sha256="70d03ee5dd9873c57beb93c399a1ddef25c063bddde6387aea821ef9cbf42565", expand=False, url="https://files.pythonhosted.org/packages/e4/2d/20aba2f7af829f9b529378061ba77c56a35761e560f0f8dc4ae4f482cdf3/e3nn-0.0.2-py3-none-any.whl")
	version("0.1.0", sha256="f1cfbd1ecd44602679f1b363a8af22d7dc4e4a7cde22cb9ba5e14df69574593f", expand=False, url="https://files.pythonhosted.org/packages/16/65/56afa3b4362a92571c72267776ea89fd61009431427bb15a254ef684ac6e/e3nn-0.1.0-py3-none-any.whl")
	version("0.1.1", sha256="980b2d16a0fc6006713aa368dcc14a97f60d9491c45437dd216cf1894a8d5d7c", expand=False, url="https://files.pythonhosted.org/packages/eb/bd/22d3d52aaa4f848364b0716a653ae8657385e271b0e31814cdb737727dd4/e3nn-0.1.1-py3-none-any.whl")
	version("0.2.0", sha256="5ac4f271dbdcef7fc75ed3497923aa232b7ddf6f806446d84fc2cb8a1ace3aff", expand=False, url="https://files.pythonhosted.org/packages/94/5b/766d1ea1032b3b3d050670a75caa588de3df3518f75f1df067e752d0c8ca/e3nn-0.2.0-py3-none-any.whl")
	version("0.2.1", sha256="81430d488337386f447b22dee3f791ed93b593d573fb2ce4fc90b7743c97d9be", expand=False, url="https://files.pythonhosted.org/packages/fb/6c/d0f25a5d6639dc32f9c6deb349018826a4a10b3ba053967ac1632411e7b2/e3nn-0.2.1-py3-none-any.whl")
	version("0.2.2", sha256="cc8047a5bc0d6c842602709974d2df6fad9cf36439fe095d8803a03c68b9f636", expand=False, url="https://files.pythonhosted.org/packages/09/60/08282bcc2d4c5d960259743a90ff4e9b8d1f1a392442b80ec9afa553d064/e3nn-0.2.2-py3-none-any.whl")
	version("0.2.3", sha256="edee46a746f5652a8e0e640e7252320b90732ebf4c2fe488d68fd8ee115ea4e0", expand=False, url="https://files.pythonhosted.org/packages/01/98/1d37a4eb19977758adcb847f8e5c5cb6906d5ffec987610c981b3ae494f6/e3nn-0.2.3-py3-none-any.whl")
	version("0.2.4", sha256="c16b8dec062a9c06ad3ab54afcc7d4d938cffff15ef96d28cd15575fa2b57617", expand=False, url="https://files.pythonhosted.org/packages/49/b8/9898ed599f16dd15f0d19bd1739f9dce8e333fdc58f97401f040d7dd5db4/e3nn-0.2.4-py3-none-any.whl")
	version("0.2.5", sha256="8e459bd12fbbdbb1b9b47e9f8a164104176f0dfa6feba9f4283f307487580eca", expand=False, url="https://files.pythonhosted.org/packages/28/de/0c1f0101327317d3dab33bcd0adb256b562ef98c2025aef0088a48f80cf7/e3nn-0.2.5-py3-none-any.whl")
	version("0.2.6", sha256="7df617ad9ba7060041b4f3d00142da83942a64f741d591e94d60d30711bcf98a", expand=False, url="https://files.pythonhosted.org/packages/7e/37/167a9f760e1b502c1d162790c507e32db5f2f113abba667928572430e832/e3nn-0.2.6-py3-none-any.whl")
	version("0.2.7", sha256="f1a20c89e770476a4257279fc1d5aee9ee5b7cf52cb40e513399a5c233a9d6b0", expand=False, url="https://files.pythonhosted.org/packages/9c/3e/32544efe098670b8d7782bc5917126ac11abdc51bf4a39668f1b660aec90/e3nn-0.2.7-py3-none-any.whl")
	version("0.2.8", sha256="ddc679b852cd3fef8e6b9aebc554c70bca09964e38e4afd192984c936f0febf1", expand=False, url="https://files.pythonhosted.org/packages/9d/87/8add263f8bc535949d3a2372aa3548b453742d268a3ed6fe9661ac696c97/e3nn-0.2.8-py3-none-any.whl")
	version("0.2.9", sha256="79800409dc4e1a82341df043897a66dd3ad61b0c401543bf9f552dc628c70436", expand=False, url="https://files.pythonhosted.org/packages/f9/39/70c645b58b30b5d756265c9e0b8b2e30b37dddebc3ab1efc12c4f0853d97/e3nn-0.2.9-py3-none-any.whl")
	version("0.3.0", sha256="03e5e7c8eb2841a1fd261cfc0d6d4650342e3b6f541ce2e82992bbe5cb2c3c3b", expand=False, url="https://files.pythonhosted.org/packages/0d/9e/20b3c004994232b0eaa87112438f72a0f0d877762af8e038097ec5d944d9/e3nn-0.3.0-py3-none-any.whl")
	version("0.3.1", sha256="9f0e208c7ae0583d5fd705dd9d49c280ebc94a7de57ed21af5c154d12d0743a4", expand=False, url="https://files.pythonhosted.org/packages/39/67/cfec0379aad0e5e1b984b7ebc7eb7f6f12808a35fa4f72ad4f5fe97c2fe4/e3nn-0.3.1-py3-none-any.whl")
	version("0.3.2", sha256="4b7a1b38a70257ecb2b72fd54412456e7e13b29bb7721a613ceb3ae4146ff2c9", expand=False, url="https://files.pythonhosted.org/packages/fb/dc/62c44bcf30a4ceb2df67e1816837a2d8c45c954fd9ec2df849ae10a53196/e3nn-0.3.2-py3-none-any.whl")
	version("0.3.3", sha256="66bd3709171da1ab97e18a0053275fa959274944b24646930fbdc50f776e13d7", expand=False, url="https://files.pythonhosted.org/packages/df/b6/393381b182a5ca04cdf4dbd4785ffbc21377301fa0c5e73407cbf5b1a291/e3nn-0.3.3-py3-none-any.whl")
	version("0.3.4", sha256="ff4925b4f17f3a5171ee0799a8980cffab124f4541d799e6e6ae753149307b3c", expand=False, url="https://files.pythonhosted.org/packages/06/e3/1a8950f70b50efbf982145a4cd79d36338f1c646a22ee557d684c5a7331e/e3nn-0.3.4-py3-none-any.whl")
	version("0.3.5", sha256="51f755102bf31d4f445ca91e93b4cb24eb6e06e3a218286b574f9394f04e8d2f", expand=False, url="https://files.pythonhosted.org/packages/60/b4/138f0f8ef3a113d09ee875e8820360575ebd991d79466d7154f11f826de2/e3nn-0.3.5-py3-none-any.whl")
	version("0.4.0", sha256="fc7a213380035bda45f29317606ab3422504f4726562c0a4dc8a133390c63757", expand=False, url="https://files.pythonhosted.org/packages/a4/da/e97c1c185facba5173dabb4efbe723656dc0888df02661889b5b8f0a6848/e3nn-0.4.0-py3-none-any.whl")
	version("0.4.1", sha256="2a1f4686e0975cfafda60503ed5c799c177bf800eb8abb89822dd60a25aa60e6", expand=False, url="https://files.pythonhosted.org/packages/66/72/4222e20e3757f4d10353ced1358a0b1dc28391bee9f4800ba1b9d2c549c1/e3nn-0.4.1-py3-none-any.whl")
	version("0.4.2", sha256="2a0ddbd818f0e7822db54e1bc48b65ce610f3a120ae2b393018b38feb5f9bade", expand=False, url="https://files.pythonhosted.org/packages/5f/cf/453bfa6243315c2b0c400d892ab501b483862c934009e500795b816f31c3/e3nn-0.4.2-py3-none-any.whl")
	version("0.4.3", sha256="61b4539781955f0e035f333dd7ce8c958a97895f642bc6d4527a0b012a9f21f1", expand=False, url="https://files.pythonhosted.org/packages/1d/2e/809fcbe843db170998bc5d70810798c7866f819de3aaf82b2de1620e780d/e3nn-0.4.3-py3-none-any.whl")
	version("0.4.4", sha256="87d99876abb362a6e07d555d10752ff2e20c2b7731d8928ebe5d9121fb019f84", expand=False, url="https://files.pythonhosted.org/packages/9a/b6/c8327065d1dd8bca28521fe65ff72b649ed17ca8a1f0c1f498006d7567b7/e3nn-0.4.4-py3-none-any.whl")
	version("0.5.0", sha256="c513cf00686204d958f9c44a997b211281ab9914ccb02224b5ce6bc6ab3446df", expand=False, url="https://files.pythonhosted.org/packages/b7/23/c2f9681ebd6afbcc0b23c16937fc7f634c42a17da2c76f98d0906ec1ad71/e3nn-0.5.0-py3-none-any.whl")
	version("0.5.1", sha256="ae064f69604f2d9f0fa07d49da02af52cb95dbea3a72869c41686d0f59a4001a", expand=False, url="https://files.pythonhosted.org/packages/f4/fe/f5b98193b0d02ccc909679ae36a0ad2d242bf7ee220a526358cf00ee2a1e/e3nn-0.5.1-py3-none-any.whl")
	version("0.5.2", sha256="5052400b8abe8dde88889d0bac5e2341b45c5f38c5c804af29752e08ecc38999", expand=False, url="https://files.pythonhosted.org/packages/9c/e8/389a80d23f4ea7fb2c4194746a877f9f969475d6a49baf7800cb9553caf3/e3nn-0.5.2-py3-none-any.whl")
	version("0.5.3", sha256="b9f20127242e447fe3a1edaa9c7e0198a2bafc66f13c7aced4398b98fc9b1c13", expand=False, url="https://files.pythonhosted.org/packages/f5/47/6b1171043f6303d7bb5500718e490bcb007bb97dcc1e876cd1ebf82a03e3/e3nn-0.5.3-py3-none-any.whl")
	version("0.5.4", sha256="4c449f727fb72037908e2eddfb0479ef756268a29b3b0ddb00ed008f0dc638f3", expand=False, url="https://files.pythonhosted.org/packages/9b/74/0ddc27c458c48890e5e668879df2987e1126a60529f175843cfc0fa42b4f/e3nn-0.5.4-py3-none-any.whl")

	depends_on("py-setuptools", type=("build"))
	depends_on("python@3.7:", type=("build", "run"))
	depends_on("py-sympy", type=("build", "run"))
	depends_on("py-scipy", type=("build", "run"))
	depends_on("py-torch", type=("build", "run"))
	depends_on("py-opt-einsum-fx", type=("build", "run"))

# {'lie-learn': ['0.0.0', '0.0.2', '0.1.0', '0.1.1'], 'scipy': ['0.0.0', '0.0.2', '0.1.0', '0.1.1', '0.2.0', '0.2.1', '0.2.2', '0.2.3', '0.2.4', '0.2.5', '0.2.6', '0.2.7', '0.2.8', '0.2.9', '0.3.0', '0.3.1', '0.3.2', '0.3.3', '0.3.4', '0.3.5', '0.4.0', '0.4.1', '0.4.2', '0.4.3', '0.4.4', '0.5.0', '0.5.1', '0.5.2', '0.5.3', '0.5.4'], 'sympy': ['0.0.0', '0.0.2', '0.1.0', '0.1.1', '0.2.0', '0.2.1', '0.2.2', '0.2.3', '0.2.4', '0.2.5', '0.2.6', '0.2.7', '0.2.8', '0.2.9', '0.3.0', '0.3.1', '0.3.2', '0.3.3', '0.3.4', '0.3.5', '0.4.0', '0.4.1', '0.4.2', '0.4.3', '0.4.4', '0.5.0', '0.5.1', '0.5.2', '0.5.3', '0.5.4'], 'torch(>=1.4.0)': ['0.0.0', '0.0.2', '0.1.0', '0.1.1', '0.2.0', '0.2.1', '0.2.2', '0.2.3'], 'torch-scatter': ['0.0.0', '0.0.2', '0.1.0', '0.1.1'], 'torch-sparse': ['0.0.0', '0.0.2', '0.1.0', '0.1.1'], 'torch-cluster': ['0.0.0', '0.0.2', '0.1.0', '0.1.1'], 'torch-spline-conv': ['0.0.0', '0.0.2', '0.1.0', '0.1.1'], 'torch-geometric': ['0.0.0', '0.0.2', '0.1.0', '0.1.1', '0.2.0', '0.2.1', '0.2.2', '0.2.3', '0.2.4'], 'ase': ['0.0.0', '0.0.2', '0.1.0', '0.1.1'], 'pymatgen': ['0.0.0', '0.0.2', '0.1.0', '0.1.1'], 'torch(>=1.8.0)': ['0.2.4', '0.2.5', '0.2.6', '0.2.7', '0.2.9', '0.3.0', '0.3.1', '0.3.2', '0.3.3', '0.3.4', '0.3.5', '0.4.0', '0.4.1', '0.4.2', '0.4.3', '0.4.4', '0.5.0', '0.5.1'], 'torch(>=1.8.1)': ['0.2.8'], 'opt-einsum-fx': ['0.3.2', '0.3.3', '0.3.4', '0.3.5', '0.4.0'], "pytest;extra=='dev'": ['0.3.4', '0.3.5', '0.4.0', '0.4.1', '0.4.2', '0.4.3', '0.4.4', '0.5.0', '0.5.1', '0.5.2', '0.5.3', '0.5.4'], "pre-commit;extra=='dev'": ['0.3.4', '0.3.5', '0.4.0', '0.4.1', '0.4.2', '0.4.3', '0.4.4', '0.5.0', '0.5.1', '0.5.2', '0.5.3', '0.5.4'], 'opt-einsum-fx(>=0.1.3)': ['0.4.1'], 'opt-einsum-fx(>=0.1.4)': ['0.4.2', '0.4.3', '0.4.4', '0.5.0', '0.5.1'], 'torch>=1.8.0': ['0.5.2', '0.5.3', '0.5.4'], 'opt-einsum-fx>=0.1.4': ['0.5.2', '0.5.3', '0.5.4']}