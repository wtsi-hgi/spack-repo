# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyFindiff(PythonPackage):
	"""A Python package for finite difference derivatives in any number of dimensions."""
	
	homepage = "https://github.com/maroba/findiff"
	pypi = "findiff/findiff-0.9.2-py3-none-any.whl" 

	version("0.0.1", sha256="24b862c27448fc802c6678d6842d9fd884d1fdee3e9d18c64dddb51042b1c9ba", expand=False, url="https://files.pythonhosted.org/packages/a5/d6/f49e4266a8ca0e0367c6e69d51cade4b7b1e4e087d2cbd074f6484fcabc8/findiff-0.0.1-py2.py3-none-any.whl")
	version("0.0.2", sha256="0dc7a80d286cba401232bb6a5d512322d1a24e4deaa9189e05f06b640e045b80", expand=False, url="https://files.pythonhosted.org/packages/d2/55/eb85e23a071286c80f97926dd6c3ba1944dcda9f2cfccb330114b60dd9a9/findiff-0.0.2-py2.py3-none-any.whl")
	version("0.1.0", sha256="5498fcee4cb03f0ce15f4728cc7c5437415190caeaf918ff7920677268a6eb8d", expand=False, url="https://files.pythonhosted.org/packages/e9/dd/2b0b534fb7d55f9b8d8ca7d64f9a4b482991aec79eccdf63e59995f3cf9d/findiff-0.1.0-py2.py3-none-any.whl")
	version("0.1.1", sha256="6225f4e82df450cdc36492a1b470b71baa1ffb01ff7105cfadb9048428cf86bf", expand=False, url="https://files.pythonhosted.org/packages/17/f2/990ecd05746fb73b3ea1c17718e97c338d0064913289f1c051dfa4d0170f/findiff-0.1.1-py2.py3-none-any.whl")
	version("0.1.2", sha256="b307be109194baba405e4f80c5dfa7c7c17e53ba51a5e5727ba5738c1b48cffb", expand=False, url="https://files.pythonhosted.org/packages/bc/f6/735b473e8defe19b3a039de629f279e54c88cd2d6f4eac7a3ce56a5d3aca/findiff-0.1.2-py2.py3-none-any.whl")
	version("0.10.0", sha256="c91180d349ab1a7d3dc2d40ea7af613efe9c9a443e397c3bd2c364a81ecbd12c", expand=False, url="https://files.pythonhosted.org/packages/34/82/256c79c7c0d72b53ac06accbb7bf52634080252bbdeedc23fb124675c99c/findiff-0.10.0-py3-none-any.whl")
	version("0.10.1", sha256="74508d24c0f35c738a3f09567c1ee31b6964c123f17704ad6c67d02b0adfb486", expand=False, url="https://files.pythonhosted.org/packages/9a/53/00c5adcf3c200356f51418949628339634c51f374ce0c5ec85595436edce/findiff-0.10.1-py3-none-any.whl")
	version("0.10.2", sha256="e3fcff5c98def160cd745bf7dcca4025015830d83973e3c540147d87b6de869b", expand=False, url="https://files.pythonhosted.org/packages/0c/a7/e3edd4b234697d1bf15b5a7cd4a45588df7198aacd68e47122a02b4d3f94/findiff-0.10.2-py3-none-any.whl")
	version("0.11.0", sha256="9985144b31ee3c2f426b45d58998d64fd41fd594df177cbb73825606f8b09fd2", expand=False, url="https://files.pythonhosted.org/packages/00/c2/d4d074bae9f9439a5f88f30e8b60034a249ead76ba3e092f860e62bd1966/findiff-0.11.0-py3-none-any.whl")
	version("0.11.1", sha256="4ae7313e8e790f3eed04f190e9755ffa6d473c9da2d2ec30b3ccc991cb58a4c8", expand=False, url="https://files.pythonhosted.org/packages/a9/d8/5a382a92cc618ad5c7e89e089f4aebb29af6870dcccdf12581ae6fd47ac5/findiff-0.11.1-py3-none-any.whl")
	version("0.11.2", sha256="f4cfc81156fdd3cfa347371200eda81643c8fbd243166d8aca25dac49bd05d15", expand=False, url="https://files.pythonhosted.org/packages/f6/7d/77bee8df3b0ed1ca9098c1c292ae96c3c10e9d47c0beb1f2ba4b0d5d015f/findiff-0.11.2-py3-none-any.whl")
	version("0.11.3", sha256="2142070e13f0499fef15b79ef2c66a94144ba49f26daf27b72084629cb9c86ae", expand=False, url="https://files.pythonhosted.org/packages/12/bb/6a5bce251ec3626d70a2cb88ddf73408280e1cef63e675d40f3fb7ef33ea/findiff-0.11.3-py3-none-any.whl")
	version("0.12.0", sha256="bd30aa7b0e26f190a4f2c69ff1b5dd2b2b8cb9996d642844806d0b243b155526", expand=False, url="https://files.pythonhosted.org/packages/9c/08/82cf59d7e7680fe4f67c19f26c7a3f5413d9c696ee75757ed9b46223268c/findiff-0.12.0-py3-none-any.whl")
	version("0.12.1", sha256="ee9573888f7b437935ae745186250be3b7c4fbac307360d614f7c20645e3a3d7", expand=False, url="https://files.pythonhosted.org/packages/62/be/5d0da13c229d798bbb668187a6188e443d2be2855e3a17c9a44b3f8dad79/findiff-0.12.1-py3-none-any.whl")
	version("0.2.0", sha256="11685b8977171217d6857ed59c5becac708b3f4a5378fcdb313e7bdf6790b280", expand=False, url="https://files.pythonhosted.org/packages/d4/0b/ebdf16cfed5c8b6501a5a920bc7162de067c96a63e39d3bdb049f6eeff42/findiff-0.2.0-py2.py3-none-any.whl")
	version("0.3.0", sha256="327d30bae9424b16070e95f7b9a5a33d629ae8c9a3e45af19feb1ea06e1980c3", expand=False, url="https://files.pythonhosted.org/packages/f2/84/f95c6cde45df12b27092edee7b48f26e333316d8aab9eab70c78bf281da9/findiff-0.3.0-py2.py3-none-any.whl")
	version("0.3.1", sha256="03e9f69707225140f7250ed2af50db0e3e77ad04bdfaddb711f3575d5477d59e", expand=False, url="https://files.pythonhosted.org/packages/de/4a/dccd4e42f4715c616a237b240c67740f9a9db1f63584420c844f08bd34c0/findiff-0.3.1-py2.py3-none-any.whl")
	version("0.4.0", sha256="b6636a0939a62baaa143d5af1bf42aceba119b4017ec3d0fcf44b57484808f7d", expand=False, url="https://files.pythonhosted.org/packages/b4/ea/1d81cf2f6b173303a8d40d5945bdc7ebba52582b8d8284236c9a9e047635/findiff-0.4.0-py2.py3-none-any.whl")
	version("0.4.1", sha256="8d789c24b994d8ca95689a269ac214afbf83b4dbecca7194950ee209e3093a15", expand=False, url="https://files.pythonhosted.org/packages/f9/ae/9d1b71e183ef21e6234ee131f55d54459b3ce44501980bccb97d184346b9/findiff-0.4.1-py2.py3-none-any.whl")
	version("0.5.0", sha256="0a50052ee08d5729baa3dd47dad337642d6908986c90979b9831857f7acde7c8", expand=False, url="https://files.pythonhosted.org/packages/f3/01/5fb4e15eaa5f6d98376120b51b2d05a2c8e8fedea7002bef1f1eb0733029/findiff-0.5.0-py2.py3-none-any.whl")
	version("0.5.1", sha256="7cf04e0d5d9bc9d7a8efb54a9135ef7adf67f299f2bd04fd9f01e511285369a8", expand=False, url="https://files.pythonhosted.org/packages/b2/ad/a4eda1cb187752f92cd831b499af65e7709fb67707804dcb5aaa535197d5/findiff-0.5.1-py2.py3-none-any.whl")
	version("0.5.2", sha256="6c2cce1e9808dc8f16b471ae66330fc6b94492e6ae4b346b1bae73a6e517344d", expand=False, url="https://files.pythonhosted.org/packages/cf/b2/dda2df02009841412e5b7e67e81bc373ddb8440a60a9e60cfbde2e7340cf/findiff-0.5.2-py2.py3-none-any.whl")
	version("0.6.0", sha256="a9187cc679c9296f9612e5e2fa9a6a734bbd462a1f042618f4bd39ff3318ce90")
	version("0.6.1", sha256="ee0af5ab9a985769939812135fa2d1e33c5a5132090c28a67c790c07b260f2df")
	version("0.6.2", sha256="cfead1d96abf965aab8fe66b634c2ddfe98e4c9f5bd4e643295d38c905714dd3")
	version("0.6.3", sha256="c255ded0f4cf60ba04666a3650de686cb5e4ebcd0742c6b6f3f307a35a5307e5")
	version("0.7.0", sha256="d24f42d67b6726e11d58233d64143fd6985a84e6c9835375277ec2ba4bb9873b")
	version("0.8.0", sha256="0ace7658c6de07791537c795a65658399039a7aad048ef0a281e6389890d28ec")
	version("0.8.1", sha256="a796a9982512077d563e12d7848802c47dc0ced34fd4c64cf168946af3541086")
	version("0.8.2", sha256="f9866a833c5a3b3b671da24c4eb48752fbf1ca855110a674d48351c5408efd58")
	version("0.8.3", sha256="0321a099fa5e288d3d1f5cefc190ede5c5d7993d24cbb2640b40f6e54f549693")
	version("0.8.4", sha256="387dd7bee676e0fa10bc5350ecb024b96533f32cc75538588886768fceb838e1")
	version("0.8.5", sha256="aa56cce0418e9e8fb648c29315a5c645536935fe79031c03212e0032461edd80")
	version("0.8.6", sha256="5909765a3d4abb6ab76d0a94c3fc1d043ec2129bfb7a31614fa5a75539d2fae9")
	version("0.8.7", sha256="b4dc987c45c6f294e12c5bb48849c380543c860e8557d9d7abf51d3f38fe07f8")
	version("0.8.7.post34", sha256="650f3be2b5cf4db30502a4a2bce6ab3a86c577443eac1e9acdb371d26835bae7")
	version("0.8.8", sha256="95e65317e300d1085a15e197f3690ad76ce58b3963a39efe366a6180790a1449")
	version("0.8.9", sha256="c89eade4ad7f7adfa3871ba00235c582ef42b6dba0e2d84c78e242be70cdbe64")
	version("0.9.0", sha256="042e05344e68a1b4f60d6ad083e28b0478161382c72eb542e14c7e7734d4c8ba", expand=False, url="https://files.pythonhosted.org/packages/1e/f4/ba33bf995a1450476e3b508ecd118301aa41724cc3917f55a17ebe2d1e7d/findiff-0.9.0-py3-none-any.whl")
	version("0.9.1", sha256="e3f66895af0605e894bf8598aef81e3b5b83cce953c75e2f87673753b591167d", expand=False, url="https://files.pythonhosted.org/packages/a0/e6/7e5c4a7e15d0e7593889d36694ab64467b79d640da969c838435ae9e62d9/findiff-0.9.1-py3-none-any.whl")
	version("0.9.2", sha256="577c1d939878b0dab8e4239f5a7f5707191c9a72e6d8803a69ac0847562f1af3", expand=False, url="https://files.pythonhosted.org/packages/60/33/265df4058a618d777f151afb6da6514f92d14fc2b0d01e8f75f734f8ea8a/findiff-0.9.2-py3-none-any.whl")

	depends_on("python@3.8:", type=("build", "run"))
	depends_on("py-numpy", type=("build", "run"))
	depends_on("py-scipy", type=("build", "run"))
	depends_on("py-sympy", type=("build", "run"))

	@run_after("install")
	def install_test(self):
		self.spec["python"].command("-c", "import findiff")
