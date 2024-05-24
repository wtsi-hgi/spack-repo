# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyVaexHdf5(PythonPackage):
	"""hdf5 file support for vaex"""
	
	homepage = "https://www.github.com/maartenbreddels/vaex"
	pypi = "vaex-hdf5/vaex_hdf5-1.0.0a1-py3-none-any.whl" 

	version("0.1.0", sha256="944cb00c26aa14ef5f0b6be8cfad7dab8f5ee4d49cd7b845f7ea09e839a38f01")
	version("0.1.3", sha256="97f64f3654250d25ef4bc442a9fa42826c68739888c3602b6bd54e260e9055b7")
	version("0.1.4", sha256="d476d8825905efe8865ac4d747a1ec07f0be50c78e2c21bafd46565a127d5cd0")
	version("0.10.0", sha256="a1fb91ee136118066f433663d76ea6e2b2eba8db8cd2830e2520ec9ed3e94512", expand=False, url="https://files.pythonhosted.org/packages/1f/d8/ac7f62ec2ad9edc1b514fc6decf2d0962719ffc5d649868eacf6b29f6b45/vaex_hdf5-0.10.0-py3-none-any.whl")
	version("0.11.0", sha256="017f05e113a5e8e09f7b8fb8312a57f3c2f1958dd5ea665fa8c4c2e86b3b2519", expand=False, url="https://files.pythonhosted.org/packages/59/3b/3736b7d1391fb4aaee4f796a185a166071597f29b9cc90056676875e80d0/vaex_hdf5-0.11.0-py3-none-any.whl")
	version("0.11.1", sha256="31799e561ccc91b754cbb18696646eb8107951701497502ccf6069f51c1392f3", expand=False, url="https://files.pythonhosted.org/packages/e6/38/f578558ec42c50e2c473fa8c0a31aa251ca64d4d4d0b6ceeb3d50acab9c6/vaex_hdf5-0.11.1-py3-none-any.whl")
	version("0.12.0", sha256="e530ee592ad2f9e55a935c31e8c48e5d827492edcc351b6a3c00f96a41b5dba4", expand=False, url="https://files.pythonhosted.org/packages/57/07/dd938aff82ffbef661e49e37156fb3866cb3d6f5d9bef66159dc8b2ed3bc/vaex_hdf5-0.12.0-py3-none-any.whl")
	version("0.12.1", sha256="c0be48c9212163ba7505dfc3c231d5729f87f3ef6397016a05144cfc95996603", expand=False, url="https://files.pythonhosted.org/packages/35/5f/0c210e637cc6267ec8d0eed3ff553332a20bc2dd4e5248bd246064e58686/vaex_hdf5-0.12.1-py3-none-any.whl")
	version("0.12.2", sha256="f94581097357a4adf5df3ef63e4571c4183661893dae25c97fb1db21e81e0e5f", expand=False, url="https://files.pythonhosted.org/packages/b7/bb/c899f4c991b31149f18f8493f208a3410a5a9f9b138fadbbdc1cca962ed1/vaex_hdf5-0.12.2-py3-none-any.whl")
	version("0.12.3", sha256="6f966fcb011e890b7777a0b3ac5c04033d99130d346c60dcf5ed609c747a640f", expand=False, url="https://files.pythonhosted.org/packages/e6/2d/60a3b5cfde43f225aa8336f14acbaccd5a35cf30a3cdd07bc44033d8bc8b/vaex_hdf5-0.12.3-py3-none-any.whl")
	version("0.13.0", sha256="61527a66ff0135f518159ad12ad91f7b1ef6364675953086163927a15a80bc39", expand=False, url="https://files.pythonhosted.org/packages/8c/9f/e31452b98b64f3191b25dc7030c177e287e5412c487d4cf542966ad1d416/vaex_hdf5-0.13.0-py3-none-any.whl")
	version("0.14.0", sha256="d0656b965f3ef95462b553eebf978e0db83ea40c40941664c9975f06367bb85f", expand=False, url="https://files.pythonhosted.org/packages/7b/e6/ad83105e10eb99eb61d154178e6c15bdfe8e267fa5d6ebe0d1f60b1b7709/vaex_hdf5-0.14.0-py3-none-any.whl")
	version("0.14.1", sha256="490c8337217e6005390dd574111d5d6d1344c2a6403e19b366c81a395d559293", expand=False, url="https://files.pythonhosted.org/packages/d3/a1/efbd153c175d2b2797a7594c81034b9e3384d47025d95caa03c739481cba/vaex_hdf5-0.14.1-py3-none-any.whl")
	version("0.2.0", sha256="49864952315808d303f2c9fa297d03a0a8c376c212b7f06fb485ff55ab81309c")
	version("0.2.1", sha256="ee47ddda6b00f40a834b9e47a5660461d92cb59223cd2e3de596b51cd0f86374")
	version("0.3.0", sha256="4d7b9bf61b821141d13a7f17b98a4b6cc2dbeaeab7dbcd4bd7c613ee750c29e7")
	version("0.4.0", sha256="c8ad4538753ec13d5ebe38b7626996f0c50998ea3ad46c6bbf0a1f7b65e22de7")
	version("0.5.0", sha256="727608e4706167853f745b556f6778c150b7e08488eedf59601c736233e6878f")
	version("0.5.1", sha256="586f03307b1f7297be462252893b71cbf732e57d4404f7dcd89fa922843451dc")
	version("0.5.2", sha256="b47ce4f0a214a29e71fc1229285fbb4c4c8685ca970fccc39e0abff933405f61")
	version("0.5.3", sha256="b1759f906bb1af10153ad3eed2edc1ff0542e19d9713b590f42f5b732adfd7ec")
	version("0.5.4", sha256="438925fd2fc1b3557d0b4ca4bd099aa8e5e98878b986eabe2670950252d0f11d")
	version("0.5.5", sha256="8d32237f72fabb8c066e90a337f739ce6417b6d52a7b597c8ea03855044f3d06")
	version("0.5.6", sha256="2418334f7b0b63ffe992e1a26d0933eb2c81ccae3dec550c2f452cdb8c9d88a8")
	version("0.6.0", sha256="369356ca054962fbaef28f33840aea7b0b0728c52e45791babb9c71b481acd37", expand=False, url="https://files.pythonhosted.org/packages/4c/b9/c590661a39ab3abdfc388ffa0392ac4cbb5fc9001c59b6ff6695840d7565/vaex_hdf5-0.6.0-py3-none-any.whl")
	version("0.6.0a1", sha256="3b4a2129394ff74627787733fe3140416a9a00fd83136591806efd28b042493f", expand=False, url="https://files.pythonhosted.org/packages/ae/94/3210e9c6f385dd0328d23d2807cc364c374d18bffc2ca574bc7bc36c4ab7/vaex_hdf5-0.6.0a1-py3-none-any.whl")
	version("0.7.0", sha256="1b7c93f8da507189f73e1d1c2eec346163b88a7aaa4e62595cc58e95fc8ba640", expand=False, url="https://files.pythonhosted.org/packages/e1/7c/7e4b11ccba78b35c28e28794c7de5847eddbc0c9b039d549beb7f277dc7c/vaex_hdf5-0.7.0-py3-none-any.whl")
	version("0.7.0a1", sha256="d549f6648279e8a6c4bbac61978015fa2fc12758cd806f736ab0eb06a0d1bce2", expand=False, url="https://files.pythonhosted.org/packages/8c/b3/a605781ed5f78ca538095f6694fb4e7b8fce713b5d5f7ddd7ea9d9ab32cc/vaex_hdf5-0.7.0a1-py3-none-any.whl")
	version("0.7.0a2", sha256="60a17ba030561300aa29c082d0917c1ef50561e3f6f6cda3952723d0817053e1", expand=False, url="https://files.pythonhosted.org/packages/bd/94/dd7d725dbb3c31bb0fceff09e5d018ad4b160356033572c1ccd7f776c513/vaex_hdf5-0.7.0a2-py3-none-any.whl")
	version("0.7.0a3", sha256="24a74de396ccfd3be391b3699fe490e3e1db5fe93fbc12aed255666e2997d114", expand=False, url="https://files.pythonhosted.org/packages/b1/8d/ae1b58aed956b633ec8ffa19f32c4d0519daab65557164c4fa2d642624d4/vaex_hdf5-0.7.0a3-py3-none-any.whl")
	version("0.7.0a4", sha256="d0b3946df85c1d02bc0d3d33ceb23223396052d13301cd0b024ebef480957046", expand=False, url="https://files.pythonhosted.org/packages/6b/99/2ab17bc7102f2fae7cbd344fe649e822eafe8c11af1fc7596bd9fdfa147c/vaex_hdf5-0.7.0a4-py3-none-any.whl")
	version("0.7.0a5", sha256="b8bcb8612989ea08d3eec022775fbbce2af63f4d4812548f0256063164d044ba", expand=False, url="https://files.pythonhosted.org/packages/ed/86/2e2de6f40c148e6cb95ad76e1a27f8450fb494b8d536a39a2c39abcce5c5/vaex_hdf5-0.7.0a5-py3-none-any.whl")
	version("0.7.0a6", sha256="588ea1c6087bc98512a57ef50ba2dc4adfb867fab5f57ed3be878fffba7d6938", expand=False, url="https://files.pythonhosted.org/packages/b0/fe/83f0f64370ce1523c82e273651642be82c41f7f8237d2b7ec885df80e1e1/vaex_hdf5-0.7.0a6-py3-none-any.whl")
	version("0.8.0", sha256="5383913dd8e9fefd70cf97ef3a05de93f7d44a079b810f4ba5beafa3f883d8dd", expand=False, url="https://files.pythonhosted.org/packages/cb/22/656285dda74d10ddf020d5e0556cb226ffea89a104ff60d7145717e33daf/vaex_hdf5-0.8.0-py3-none-any.whl")
	version("0.9.0", sha256="72f2ff08428d8622bb4aff25e0a85c9c228dc6d67192c6e1eb2f45a8ff6c8e2d", expand=False, url="https://files.pythonhosted.org/packages/c0/09/4ea21c6b0a30fa9380263fc5b741ea4c125e17d3cd38cef641e511159659/vaex_hdf5-0.9.0-py3-none-any.whl")
	version("1.0.0a1", sha256="fbb5d04c292605e67bbb47f7aa9b48a95e1fc4b5a90dd6703863772775d34f25", expand=False, url="https://files.pythonhosted.org/packages/e9/ac/e345235f586ddd672b409282ee8d98756c0645346da16d84c21a4ed128ec/vaex_hdf5-1.0.0a1-py3-none-any.whl")

	depends_on("py-h5py", type=("build", "run"))
	depends_on("py-vaex-core", type=("build", "run"))
