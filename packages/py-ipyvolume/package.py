# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyIpyvolume(PythonPackage):
	"""IPython widget for rendering 3d volumes"""
	
	homepage = "https://github.com/maartenbreddels/ipyvolume"
	pypi = "ipyvolume/ipyvolume-0.6.3-py3-none-any.whl" 

	version("0.0.10", sha256="2c67a73ff2f06145d413bd779935d3eaa48befb26cc92dd0004a78c6a6dcd514")
	version("0.0.11", sha256="876da447373a7b877c07e4ca8922c8ead0943c26f3f8398d83d8bbdcfc48d3d5")
	version("0.0.11.post1", sha256="d49dcfded49969cfbd77f61f175f698b66beef3374119e09c6896a7e06e67d9d")
	version("0.0.12", sha256="cc994bfc1cfe3c8d3a60db4b763bd03dbca46dffa7f9a147daa0930c0d73f505")
	version("0.0.5", sha256="3d789bdc405efecccdf5370a770ed1d4f804d121d6f33b0f1b1c1843fe633285")
	version("0.0.7", sha256="da8991c64208147e5bb1beff542e86632bbcd9fccdcaf324afd15f4c86f38d44")
	version("0.0.8", sha256="77c1bbc430766c5ed201c833c6777b30f4987299c1c0bd7d375d0b6157813642")
	version("0.0.9", sha256="20944fc8a82c2cbd98dd9d9fac74aa91cabee06f51471c8ce8e771233bd9990e")
	version("0.1.0", sha256="ea4b0fa88a0424071fa4b8a4dcd8a66ae6d9ed0e59774f7c5c5d48b96ad4886f")
	version("0.1.2", sha256="02a56309e69cbe9885589f80d7503bfb5ae558df29db1d2ca0ef0471aaef558a")
	version("0.1.3", sha256="5a7883c172d4e007e9a188ec60341da5444e358753725aa8cf6df81036b93cb4")
	version("0.1.4", sha256="d041ab0f7db0c27f0efbabb2cb36258c24d9201d583b64a993cc902c812a4f07")
	version("0.1.6", sha256="60864348f8078a7d0e8d0a6c41fb5303acad4200d660c179c6dff98fb97057f0")
	version("0.1.7", sha256="61b730f866b699931b05679e6fb01758a5cbb7d4f994f6a42dec6446665f9d07")
	version("0.1.8", sha256="435652d55572284f1ad04747eabfc3542c5a4dd8f56ce4a93cf32f9fa2a9ff90")
	version("0.1.9", sha256="096cef24cd0862739f78478cc1a51c1e6cdf99546299e886c3475dc13b967a61")
	version("0.2.0", sha256="74e30e740f20c40bfc89322213766f767eea64bff99cb78968f70b394e3ab61d")
	version("0.2.0b1", sha256="142c9266f978747514cc361946f5359a1be1ec6f21cca7a327e5107843d477ed")
	version("0.2.1", sha256="8da76c8b35422464e776ec2eaf4c59531ed50020467c0765663be65885853e85")
	version("0.2.2", sha256="e92c41028acc2a8aec7075ae540a9ad3df82f2e8ecbe5cdfdbe4a43d27705f5e")
	version("0.2.3", sha256="3bf08792e6ad5facc190b3f7d70e0fd0a3840fe2c5b48331d2d7215d6e6e97f7")
	version("0.3.0", sha256="3ad5f6b2e7548be28106a7c64a9507532bb40a4b64778f8b3f2c89ca3adbac76")
	version("0.3.1", sha256="52631018cef037267de331c20541bc109d28533675dd220c39fccfe913df5c95")
	version("0.3.2", sha256="165f0f1f60457b64d01400816e0e19bc9f304a63bc06755a4ca6457c8be238c3")
	version("0.4.0", sha256="8f6f5a56ebbecbff76f35115040776dee6c638aa64ca6235ddf3066c89d5e09b")
	version("0.4.0a1", sha256="7707f8131c8eb440ee5551c53ff6cc6aa5574dbf2e170af2b547b1aba8f2d108", expand=False, url="https://files.pythonhosted.org/packages/a8/85/dd0a2d39aa3760bfffa832a24ef7727940b133343c538020fc435aa7c88c/ipyvolume-0.4.0a1-py2.py3-none-any.whl")
	version("0.4.0a2", sha256="88c8d69fb2a6bd954fb0aaa79b1371b3f15548adc3c4eae432c84f62a6060c5a", expand=False, url="https://files.pythonhosted.org/packages/20/0e/b4400452fd8a96f05d42dd5071d2b42324a15f29599b00f06643d6398010/ipyvolume-0.4.0a2-py2.py3-none-any.whl")
	version("0.4.0a3", sha256="8dc17f916df31f285f9367f40136ffa1ae25a42ec042aab314b97a3011e02bba")
	version("0.4.0a4", sha256="e037e1695b939e62d45e515c3c129731bb27c6196207cc8d3029f4b0d6c8e573")
	version("0.4.0b1", sha256="c39e9fa65d562b2c955d7f35a76547b68493277835bb67221c833255f89b4449")
	version("0.4.1", sha256="6f804e6547a346eb5e25cacbcb552ccbc0636a0e7de5ca771150c1b99ae7b9ca")
	version("0.4.2", sha256="738738d104899c046913041c3f92aa3ac274f4127bd8e052120be21f32f4eddd")
	version("0.4.3", sha256="a37f08b8d35a319c92e5055ec14a1b64d641722c3f6f59ddccd77cf550fbcb12")
	version("0.4.4", sha256="c92f182890f426d83908a655acec3b0f6c9196cfeb1ea25e299340abc8b4f8a8")
	version("0.4.5", sha256="90de0c2e3fb9e3d234f6a80c2cffbec8100ce9061cf459758c77b8054d1312dd")
	version("0.4.6", sha256="a4e570305655c9c213bf7dbee869192692cee6cdc809a713c192ff57b15a3189")
	version("0.5.0", sha256="f5c606214cbf86e326032a547f4565f8e987d7d36a40b475057e0919697af3f0", expand=False, url="https://files.pythonhosted.org/packages/38/32/951b27dda9e56a95ca5d8bfbdb63f8c189b84bc27e3bd2c7a4404ea6ec8c/ipyvolume-0.5.0-py2.py3-none-any.whl")
	version("0.5.0b1", sha256="659a300af502499eac6b0c6f6c37299177dde1f4169b42b07636deccf0a3c474", expand=False, url="https://files.pythonhosted.org/packages/10/a6/59239560e94f7a814399b82de7732150175cdcc53d579b6e49919fd48f6b/ipyvolume-0.5.0b1-py2.py3-none-any.whl")
	version("0.5.1", sha256="b31b6f3d7bae040ce8326ddd0e25bd0e8951e9b77e5f040e9b017bf6db047b7c", expand=False, url="https://files.pythonhosted.org/packages/6c/e4/4a6754d2c390ee627f82aeaae76b34a1daf30eea80af41215eebedb0f5ce/ipyvolume-0.5.1-py2.py3-none-any.whl")
	version("0.5.2", sha256="dccae36f5744bf262ea3f0367e36e341290847b3da37928cb86197380d8c8257", expand=False, url="https://files.pythonhosted.org/packages/c4/be/09982f3bce56da844c5ee4642a8bfae9908e61d7e6999e7e91479cc64b6a/ipyvolume-0.5.2-py2.py3-none-any.whl")
	version("0.6.0", sha256="7a6046d13525eb0e3bde970ed81236cd3930903e6a070f82d9d3501a4c6b51b1", expand=False, url="https://files.pythonhosted.org/packages/31/cd/4558832c3974ba18a447f6a6143bb4a9b4c5566fb6fc0d8d839c48eaf0d2/ipyvolume-0.6.0-py3-none-any.whl")
	version("0.6.0a1", sha256="f2e2e69e5fdeea33dd8fa7eb2f13c36d9fcca9dec9415ded944b14486bd1fd1e", expand=False, url="https://files.pythonhosted.org/packages/d1/f2/7cd5bc0c5ca85c2d4b9a4595e1864cb6bc828a11340507974c649eba8564/ipyvolume-0.6.0a1-py3-none-any.whl")
	version("0.6.0a10", sha256="9838a090f25ef17f88774c86ac5585687b5834ea82ef67afe9d410205f1766da", expand=False, url="https://files.pythonhosted.org/packages/2e/7e/6b530ab92d92c2b35bc46a9591363994b2f87ecb40b6e4afc12a039db112/ipyvolume-0.6.0a10-py3-none-any.whl")
	version("0.6.0a2", sha256="9124c01b94aa43a8d639797bff22c1fc80a6dcc192e89410eaf22e906d2cf2f7", expand=False, url="https://files.pythonhosted.org/packages/39/f5/db5a15770d0d8e845830b40756e1c55af833d7d8494f96bd9cfca911aa19/ipyvolume-0.6.0a2-py2.py3-none-any.whl")
	version("0.6.0a3", sha256="9111dfeeb3b719db069342cc0975f1601732322a5882b89c36ddc4da8419cdde", expand=False, url="https://files.pythonhosted.org/packages/04/66/29a7b3fcd81d05b3b2bcfb9cbec28e6ec6838201332665ad42fb38a2d773/ipyvolume-0.6.0a3-py2.py3-none-any.whl")
	version("0.6.0a4", sha256="025d57a6b284a887765343bd861b20145ceac1c6fea1649ce490c96c06b05a38", expand=False, url="https://files.pythonhosted.org/packages/5c/f5/be04eb3050fb18982e4e9f9eb937800c4d398576b4b2f2fe40b152f8cf54/ipyvolume-0.6.0a4-py2.py3-none-any.whl")
	version("0.6.0a6", sha256="5796cd890414c765cce7c6e6415b80901dde3a511c83b504eb42817742b0feed", expand=False, url="https://files.pythonhosted.org/packages/eb/b3/c4c74424d2d53fd31c57d6e946c3d993c4bf0b8f3b1f0a6272f94ddd75ed/ipyvolume-0.6.0a6-py2.py3-none-any.whl")
	version("0.6.0a7", sha256="bfaf678ce2db5f3b6301877b8721a6c35fe441160b0402d97100179b8ec073b3", expand=False, url="https://files.pythonhosted.org/packages/10/63/16b59ccf9ea55a84b5081e913e80595356673359c28f6da2cae98e834dc6/ipyvolume-0.6.0a7-py3-none-any.whl")
	version("0.6.0a8", sha256="ee0f1d7919e61494a07989d2a8f816cf335d050d47a0240e9d2490266a6aff9a", expand=False, url="https://files.pythonhosted.org/packages/80/19/4e1afbe1aaad95b7d6a9c1e907e01cbd344d7b2b94c8ad1036b529de76c6/ipyvolume-0.6.0a8-py3-none-any.whl")
	version("0.6.0a9", sha256="005113e03af8164deb416f86def87f0977dda7bff46bcc593f1e2e4fc11ea27c", expand=False, url="https://files.pythonhosted.org/packages/1d/61/a7cef0e686cb36fec40da433fc7070120086c1f7667a51536c4f2b83db0a/ipyvolume-0.6.0a9-py3-none-any.whl")
	version("0.6.1", sha256="b8d3baf5bf2cbb7708955ae706a85502fd0d04435793ceb558b578e4f51f9b84", expand=False, url="https://files.pythonhosted.org/packages/31/97/51d03e07e0f134c068b0c4671049344a137e04a99b2837d434f41f1f52d9/ipyvolume-0.6.1-py3-none-any.whl")
	version("0.6.2", sha256="17747dae229e43bc081856c44a3f8b3df0609b63fb8a64f947ad4391835b9a6c", expand=False, url="https://files.pythonhosted.org/packages/5d/c9/eddf08214fbdb2930bdfdd82efb5b73ef2068918084af4507ba265532557/ipyvolume-0.6.2-py3-none-any.whl")
	version("0.6.3", sha256="550761b5cc1a9fb0e8931056fd523b2f0074ddea46633a248f996168e5b0d7f6", expand=False, url="https://files.pythonhosted.org/packages/88/ca/153406ca7ff41ea3ecf8c3b5c0db07364461e867fb197b1723bf0be2652d/ipyvolume-0.6.3-py3-none-any.whl")

	depends_on("py-matplotlib", type=("build", "run"))
	depends_on("py-pythreejs", type=("build", "run"))
	depends_on("py-ipyvue", type=("build", "run"))
	depends_on("py-ipyvuetify", type=("build", "run"))
	depends_on("py-requests", type=("build", "run"))
	depends_on("py-ipywebrtc", type=("build", "run"))
	depends_on("py-pillow", type=("build", "run"))
	depends_on("py-traitlets", type=("build", "run"))
	depends_on("py-traittypes", type=("build", "run"))
	depends_on("py-numpy", type=("build", "run"))
	depends_on("py-bqplot", type=("build", "run"))
	depends_on("py-ipywidgets", type=("build", "run"))
