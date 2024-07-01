# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyJanus(PythonPackage):
	"""Mixed sync-async queue to interoperate between asyncio tasks and classic threads"""
	
	homepage = "https://github.com/aio-libs/janus"
	pypi = "janus/janus-1.0.0-py3-none-any.whl" 

	version("0.0.1", sha256="e99c6e3d2737d4446668ecc02670c38a3cef4d34bf347c5bff49a66b21dd20b2", expand=False, url="https://files.pythonhosted.org/packages/a7/d8/e0e4335f06ba04e812aa8cc7a480768cdc9758355e4b73cc711bb566b02a/janus-0.0.1-py3-none-any.whl")
	version("0.0.2", sha256="1e45e4c9015c34f10d9512351b0a4f67de8ea696b0a28bea4444923a72b68496", expand=False, url="https://files.pythonhosted.org/packages/98/ea/0d8582422a430b3940b1b12655ec384cc63b8df53d18b9d80c2cffaf879f/janus-0.0.2-py3-none-any.whl")
	version("0.1.4", sha256="b55c1dae43cc20267cd455253c2d9a982598c725bd7b0e27f37b538353e6bfc5", expand=False, url="https://files.pythonhosted.org/packages/42/b0/ed154319bff7007e4275e69808a6a3e33605d077415b15e312594c504769/janus-0.1.4-py3-none-any.whl")
	version("0.1.5", sha256="641d7a4c6ef5596c349b1c19abb48c1b8a55a3e35b49062cfb4053be40240b93", expand=False, url="https://files.pythonhosted.org/packages/ae/a6/3eccf6a82db824fb071c8ffc3cbb8b92a099f99cd20c8a49829002e6bfca/janus-0.1.5-py3-none-any.whl")
	version("0.2.0", sha256="edadab771a7137293aa68a45eb31a855b6015ee546c1db3ac4ebcb1a13fd974f", expand=False, url="https://files.pythonhosted.org/packages/25/89/e6a1d0b6ea108f8137711ed361c94b3a3b6e5e9f16aaad1153c2d4881be6/janus-0.2.0-py3-none-any.whl")
	version("0.2.1", sha256="46048a562222507d3279589f72d5e5582461483039e932151aecfcecb894258f", expand=False, url="https://files.pythonhosted.org/packages/7e/87/1560cc5f1c60c57079fa31a776918cdf97a4461b785ebe6be29e62e24dd3/janus-0.2.1-py3-none-any.whl")
	version("0.2.3", sha256="82012c12c2e506ecc0ef34b6efa5e8987358ab66b16e1504acbc395f231d34ed", expand=False, url="https://files.pythonhosted.org/packages/18/78/48d30d794a851869c5800f36c4fca50611ae55fabe11c88ab012bff2a1fd/janus-0.2.3-py3-none-any.whl")
	version("0.2.4", sha256="d7416707317b58f725e885845496dad63a581da8f3ebcedbb41c084b0912181d", expand=False, url="https://files.pythonhosted.org/packages/6d/b2/9b4a85c380264f0aca717acc98b5b62f5c13576b4dc13073320f6715a94b/janus-0.2.4-py3-none-any.whl")
	version("0.3.0", sha256="1a6b1d1e521a91fcaf3e064b65d0ae133dd6d3dc8102e49a86ada25c6286dd48", expand=False, url="https://files.pythonhosted.org/packages/5f/81/231bd92a8f74d99c936ef5d916f87884444d59a7483a3529cedfcec38d5b/janus-0.3.0-py3-none-any.whl")
	version("0.3.1", sha256="ceccb46adc15635b9e33a13ee340d461dc9ce68475f056b20459f9715baf064e", expand=False, url="https://files.pythonhosted.org/packages/21/07/0b7f5ecb654e783ed8c9f603185917f3c35431b98784d81d858ec9f70e79/janus-0.3.1-py3-none-any.whl")
	version("0.3.2", sha256="e763ab580580010862ffeec49dbe5c1fee232d361994fd43fb11c13cbb527594", expand=False, url="https://files.pythonhosted.org/packages/3e/4c/d7d25bd2cddd5298291622dc6e19fd8c23a833255fe53bfa40f1349ba53f/janus-0.3.2-py3-none-any.whl")
	version("0.4.0", sha256="86878806559274376b83193bfd992ad94576d1024ddfc69cf1a908bf20d6b37d", expand=False, url="https://files.pythonhosted.org/packages/1d/9e/e52b01cca283a6b75e817cb85121ad921a70d129581d89190ef584296180/janus-0.4.0-py3-none-any.whl")
	version("0.5.0", sha256="f35c78f9cd13899438cce525e6ebabc7f8ad5f1b26b2f7d9ae153b4499acc84a", expand=False, url="https://files.pythonhosted.org/packages/f0/18/14dbe19f4af1350965b79d0cdc69cc16460fe7a9ed701d2941294b1e3557/janus-0.5.0-py3-none-any.whl")
	version("0.6.0", sha256="3c7b56681de4c115fea76a933b7be5ed783e4b7c7922e9973751ad66806a0e03", expand=False, url="https://files.pythonhosted.org/packages/7f/04/868183650beb3d66a027d1b0f75fb3ac43cb0e0cd57817b703100ba78453/janus-0.6.0-py3-none-any.whl")
	version("0.6.1", sha256="6dae3f1fd68a92dab49c1b93d269f22d2232feddf3a3b8842a881a6e67500c16", expand=False, url="https://files.pythonhosted.org/packages/58/c4/802a3f74f5d9176a2ba9a838a5f5fb365acabfc0b3e6a1e3e4f91c09c85e/janus-0.6.1-py3-none-any.whl")
	version("0.6.2", sha256="a719e6b0bed81a5d64fef0c186ee44b3077812b03e6f86deccab13e37ade33ec", expand=False, url="https://files.pythonhosted.org/packages/04/51/fc88d660980c7087310c65cbe3005a3eb0907e64eb9b217c2d44e91faf47/janus-0.6.2-py3-none-any.whl")
	version("0.7.0", sha256="41e267f50b10f981c1d29f9fd065ec27086d32f823cefb39808ba7887b39f860", expand=False, url="https://files.pythonhosted.org/packages/57/f8/91caa9e4ee5e1cdd1d8dccad11e851634ba44a274e391d27b0a8655b81f7/janus-0.7.0-py3-none-any.whl")
	version("1.0.0", sha256="2596ea5482711c1ee3ef2df6c290aaf370a13c55a007826e8f7c32d696d1d00a", expand=False, url="https://files.pythonhosted.org/packages/c1/84/7bfe436fa6a4943eecb17c2cca9c84215299684575376d664ea6bf294439/janus-1.0.0-py3-none-any.whl")

	depends_on("python@3.7:", type=("build", "run"))
	depends_on("py-typing-extensions", type=("build", "run"))

# {'typing-extensions(>=3.7.4.3)': ['0.7.0', '1.0.0']}