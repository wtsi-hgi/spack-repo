# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyNestAsyncio(PythonPackage):
	"""Patch asyncio to allow nested event loops"""
	
	homepage = "https://github.com/erdewit/nest_asyncio"
	pypi = "nest_asyncio/nest_asyncio-1.6.0-py3-none-any.whl" 

	version("0.9.0", sha256="0b6822ccd42f01b8697a4644ba68f84fbbf8a9df196debda4634aedf2ecde80a", expand=False, url="https://files.pythonhosted.org/packages/1b/74/c175e6a66c2f42de82c03910ba2909dd452c796fbdf22203bf2a35957b0d/nest_asyncio-0.9.0-py3-none-any.whl")
	version("0.9.1", sha256="b74617777d5746427b641ec08bb98023f36fcadf419b1de2eca45ff27f1ceadf", expand=False, url="https://files.pythonhosted.org/packages/22/9a/4d76c36f57847ed655836022f42a36ef19bb44f519278c37edab79d7cfdd/nest_asyncio-0.9.1-py3-none-any.whl")
	version("0.9.10", sha256="53c9052eaca92d3f138581b8ff0e40c2e7efa155f5455bdf901f5652b4ee8abe", expand=False, url="https://files.pythonhosted.org/packages/ed/33/bd5795e49e80a7f7af01c579c15fc567b38ece001c9fe98675544fb48e19/nest_asyncio-0.9.10-py3-none-any.whl")
	version("0.9.2", sha256="5c8cd3716ddb7313c77d6eb133c1ac4da317708564b2cc5b90663c4bd095c90f", expand=False, url="https://files.pythonhosted.org/packages/0a/e9/9cee04a86f91b1eba1288ffc228948e2d61e6ca3ef3cdc389a794ba8cb85/nest_asyncio-0.9.2-py3-none-any.whl")
	version("0.9.3", sha256="6eb62ae5127cccd6afbecf4216a8a8350bb0135daa3ce16bd67cbd0d1f4d7974", expand=False, url="https://files.pythonhosted.org/packages/19/17/22a12192d5db46f06deb6f10d144f746277821830d9cd94e72cb517a21e1/nest_asyncio-0.9.3-py3-none-any.whl")
	version("0.9.4", sha256="0127c9ff8a7dc83801d08bd72e4a730ab8d228c0f74754b3ae601229f49cbf55", expand=False, url="https://files.pythonhosted.org/packages/23/4e/e2498477e40415d6c5226db491f636e3285e6afcbca20284735fc0dbdda9/nest_asyncio-0.9.4-py3-none-any.whl")
	version("0.9.5", sha256="43492244e41e37d408dbc57d8e6c40755cb37622a6f030b41e9dff6eb72acb12", expand=False, url="https://files.pythonhosted.org/packages/bd/75/42d31d42bbdded0621c741c49b4b978c2c40fb6db4b95e3c3abe176cbcff/nest_asyncio-0.9.5-py3-none-any.whl")
	version("0.9.6", sha256="3b6eead8307e21c4aed7702e7d245c73aafa041cfd58638e7cde7bf9442f83ae", expand=False, url="https://files.pythonhosted.org/packages/80/a0/90fe74e8ad82e34d7bdb983f2f7a276886fadf8d98646adb52a594899ab5/nest_asyncio-0.9.6-py3-none-any.whl")
	version("0.9.7", sha256="6cafd7891d795a4b90fcc0358618b2ebe763ad5734220e8c8aeed8205b313f9a", expand=False, url="https://files.pythonhosted.org/packages/fa/0d/ee83bc61c588e272614b663d4acef7ccec9984dad8d2decd71fb9eb6144c/nest_asyncio-0.9.7-py3-none-any.whl")
	version("0.9.8", sha256="81ff35e78f28d6caf70b85c8823b877f4cda74d78c947c2e81178d6c96e87700", expand=False, url="https://files.pythonhosted.org/packages/d5/21/59aacdea7146be7a9a6dcc90676a4b601f9396c720b0df754108f75e7953/nest_asyncio-0.9.8-py3-none-any.whl")
	version("0.9.9", sha256="c902e2290cce61452de2ffa080c56e2cded04caf71aea4466e78234d7e62e486", expand=False, url="https://files.pythonhosted.org/packages/f4/e0/1e421f35db33185567a1ef291ca2c359e739ec795c5ff487a03e85df7e74/nest_asyncio-0.9.9-py3-none-any.whl")
	version("1.0.0", sha256="485a69ec0b96fa2da676913c5047de929742878eac4cbcefbe222bc499d7998b", expand=False, url="https://files.pythonhosted.org/packages/62/18/4c6a895c925e8822e72535d774861e9ca07089c4b938ed20002b1aaab66a/nest_asyncio-1.0.0-py3-none-any.whl")
	version("1.1.0", sha256="510159bf7b14faa88edf2725a53910b2c5c5cc1231435c1c6d97632daa1ed21b", expand=False, url="https://files.pythonhosted.org/packages/09/82/76dfcb16ba761a70bc89d93c6af2d13c1677f04bb8fa70213685ee071588/nest_asyncio-1.1.0-py3-none-any.whl")
	version("1.2.0", sha256="1bf4bbda9d71a436e995356ee9443dd6f966e777735c99c6da5a5d15f5a4b759", expand=False, url="https://files.pythonhosted.org/packages/81/f3/e59eb5fa5c41c7e6ae9741ed18534dbfae15ad29040a3927396678934b28/nest_asyncio-1.2.0-py3-none-any.whl")
	version("1.2.1", sha256="c5e710ef96b1f490f2facb47780314810c7131d695cddf829516c3ffd54beb83", expand=False, url="https://files.pythonhosted.org/packages/52/01/55100e0dda328f2181b719bddc5af0a24487de81038747d676d5be7ef879/nest_asyncio-1.2.1-py3-none-any.whl")
	version("1.2.2", sha256="0a05c8dbd27a02d14da773333c98ea069dee8079f8de7acb60dd0f46bfa2f845", expand=False, url="https://files.pythonhosted.org/packages/88/51/1543cc12c3270874411b248e3e23f18ec8af5b2f2d82b6241c5ea17c2648/nest_asyncio-1.2.2-py3-none-any.whl")
	version("1.2.3", sha256="e2c7c04b0ffd994fb1561b60d9c14cd6138eabd0a918c7626de887b159255d20", expand=False, url="https://files.pythonhosted.org/packages/ad/05/a511d3c77850879409ca8a5f73257da50b97c28e030a82cdf8b0d359dedf/nest_asyncio-1.2.3-py3-none-any.whl")
	version("1.3.0", sha256="57bb3b784832912384b8525aea4b6a51a97cf0797b9291404f73669db08c2f24", expand=False, url="https://files.pythonhosted.org/packages/80/c2/45c9fc4512608b0da793cb43765aca5f609715c28e5c63a1209dde3be80f/nest_asyncio-1.3.0-py3-none-any.whl")
	version("1.3.1", sha256="fb5129b486488c1b783918c6e3044df0a6f6971454a33dcda8276578d8ac6a73", expand=False, url="https://files.pythonhosted.org/packages/d2/9f/68e5554be28874a79b5a90f63da28738b15a9da7889c41c7033eecd7522d/nest_asyncio-1.3.1-py3-none-any.whl")
	version("1.3.2", sha256="b4cdd08655e2848098d204a26590cbfa39fcbc4ad1811c568678ffc8a0c8e279", expand=False, url="https://files.pythonhosted.org/packages/fb/98/f4add7297a8d586fe7ac756707673d03d97b9ed7c171291bb43889dbfbc5/nest_asyncio-1.3.2-py3-none-any.whl")
	version("1.3.3", sha256="766ee832cdef108497a70dd729cc4ff56d16a8d3e08404ae138bdf15913f66f9", expand=False, url="https://files.pythonhosted.org/packages/74/b4/b24e0a271fb78990c2c62238321686454824b1357ce7abcf20f431fd903d/nest_asyncio-1.3.3-py3-none-any.whl")
	version("1.4.0", sha256="ea51120725212ef02e5870dd77fc67ba7343fc945e3b9a7ff93384436e043b6a", expand=False, url="https://files.pythonhosted.org/packages/a0/44/f2983c5be9803b08f89380229997e92c4bdd7a4a510ccee565b599d1bdc8/nest_asyncio-1.4.0-py3-none-any.whl")
	version("1.4.1", sha256="a4487c4f49f2d11a7bb89a512a6886b6a5045f47097f49815b2851aaa8599cf0", expand=False, url="https://files.pythonhosted.org/packages/a0/68/c917f9679b3206952e13e95434d6e70dacea13161dff3476fa088e610987/nest_asyncio-1.4.1-py3-none-any.whl")
	version("1.4.2", sha256="c2d3bdc76ba235a7ad215128afe31d74a320d25790c50cd94685ec5ea221b94d", expand=False, url="https://files.pythonhosted.org/packages/c7/41/383505cff32a503179e3ec0612962447a83e3f201742b6f7c27c14f54fc5/nest_asyncio-1.4.2-py3-none-any.whl")
	version("1.4.3", sha256="dbe032f3e9ff7f120e76be22bf6e7958e867aed1743e6894b8a9585fe8495cc9", expand=False, url="https://files.pythonhosted.org/packages/5c/33/10805a3359f56ac4f3b520e64b9d5e6a288d87be95777b8023c64cba60f1/nest_asyncio-1.4.3-py3-none-any.whl")
	version("1.5.0", sha256="e5e42f7c6b03a0f22e9e65ffae5665a07d24f0dc1aa057e5a0e2476c4a30aa69", expand=False, url="https://files.pythonhosted.org/packages/aa/32/1d7bcc1a5c86cbbf62a03209088ebb287b0639a384fc13db79ad82c03cff/nest_asyncio-1.5.0-py3-none-any.whl")
	version("1.5.1", sha256="76d6e972265063fe92a90b9cc4fb82616e07d586b346ed9d2c89a4187acea39c", expand=False, url="https://files.pythonhosted.org/packages/52/e2/9b37da54e6e9094d2f558ae643d1954a0fa8215dfee4fa261f31c5439796/nest_asyncio-1.5.1-py3-none-any.whl")
	version("1.5.2", sha256="21b4e6b9ee3fe9108a048e6f6f2f1bdc5d9926022c6c4592d668ea3493784d46", expand=False, url="https://files.pythonhosted.org/packages/6c/2b/21d0ee1c44f80ef3293ae9a6a8a54a1f1e43bdb39e1f5e4a82f22d0f21f5/nest_asyncio-1.5.2-py3-none-any.whl")
	version("1.5.3", sha256="54f61b6563a592111f16c3e00cfb25ba4bc502adea8c0ee08d72bbdacc0009cd", expand=False, url="https://files.pythonhosted.org/packages/37/05/bc7b5dd2fc4f396c43697f1a3f138902b20b2930c27713d71400acbafba3/nest_asyncio-1.5.3-py3-none-any.whl")
	version("1.5.4", sha256="3fdd0d6061a2bb16f21fe8a9c6a7945be83521d81a0d15cff52e9edee50101d6", expand=False, url="https://files.pythonhosted.org/packages/06/e0/93453ebab12f5ce9a9ceda2ff71648b30e5f2ce5bba19ee3c95cbd0aaa67/nest_asyncio-1.5.4-py3-none-any.whl")
	version("1.5.5", sha256="b98e3ec1b246135e4642eceffa5a6c23a3ab12c82ff816a92c612d68205813b2", expand=False, url="https://files.pythonhosted.org/packages/be/1e/a83058de46b40a392bdefcaac44d1d42db4bf8562cb68c95d6bae4b93276/nest_asyncio-1.5.5-py3-none-any.whl")
	version("1.5.6", sha256="b9a953fb40dceaa587d109609098db21900182b16440652454a146cffb06e8b8", expand=False, url="https://files.pythonhosted.org/packages/e9/1a/6dd9ec31cfdb34cef8fea0055b593ee779a6f63c8e8038ad90d71b7f53c0/nest_asyncio-1.5.6-py3-none-any.whl")
	version("1.5.7", sha256="5301c82941b550b3123a1ea772ba9a1c80bad3a182be8c1a5ae6ad3be57a9657", expand=False, url="https://files.pythonhosted.org/packages/7e/dd/69a7a6e89bb1fe09f99bde22027154c487b1e8b6769e642d7f56f35696d3/nest_asyncio-1.5.7-py3-none-any.whl")
	version("1.5.8", sha256="accda7a339a70599cb08f9dd09a67e0c2ef8d8d6f4c07f96ab203f2ae254e48d", expand=False, url="https://files.pythonhosted.org/packages/ab/d3/48c01d1944e0ee49fdc005bf518a68b0582d3bd201e5401664890b62a647/nest_asyncio-1.5.8-py3-none-any.whl")
	version("1.5.9", sha256="61ec07ef052e72e3de22045b81b2cc7d71fceb04c568ba0b2e4b2f9f5231bec2", expand=False, url="https://files.pythonhosted.org/packages/0d/d0/ffa604feb4992d5ecb3a0581df1afa6f5a05027c29c49db867acd7e4e10e/nest_asyncio-1.5.9-py3-none-any.whl")
	version("1.6.0", sha256="87af6efd6b5e897c81050477ef65c62e2b2f35d51703cae01aff2905b1852e1c", expand=False, url="https://files.pythonhosted.org/packages/a0/c4/c2971a3ba4c6103a3d10c4b0f24f461ddc027f0f09763220cf35ca1401b3/nest_asyncio-1.6.0-py3-none-any.whl")

	depends_on("python@3.5:", type=("build", "run"))
