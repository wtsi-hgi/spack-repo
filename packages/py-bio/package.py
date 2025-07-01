# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyBio(PythonPackage):
	"""Making bioinformatics fun again"""
	
	homepage = ""
	pypi = "bio/bio-1.8.0-py3-none-any.whl" 

	version("1.0.2", sha256="c8f6224b4db27f0fa441c34b8e909b0587b6937a4304807494ecfb1fe46a2630", expand=False, url="https://files.pythonhosted.org/packages/75/1d/21f024f1a13ff94729305c4a96ed074d7dd8a6c3b0cd34197cc1e44ecf57/bio-1.0.2-py3-none-any.whl")
	version("1.2.0", sha256="c30abab4ae8a4033410ef0ca1450135c540366852f8c0f76d44564aedb7f06ea", expand=False, url="https://files.pythonhosted.org/packages/3d/74/0846a323a2ce7fe5839d36144ee6ba06882a8a89837831408e62f3947580/bio-1.2.0-py3-none-any.whl")
	version("1.3.2", sha256="eaf03a66252b92cac1eb77f75e06c5ded8d5db06d5eb15c4b29dbb50101500b0", expand=False, url="https://files.pythonhosted.org/packages/52/18/ed1942f57e2748ab4805270ddd99df0aea47ab2b189b603017cb37dc9664/bio-1.3.2-py3-none-any.whl")
	version("1.3.3", sha256="d56bd5f00018a04a8b777f86ab1ffac794a65ba925dcd188a46a9b1db74f58cf", expand=False, url="https://files.pythonhosted.org/packages/87/82/3a2c9643c180743b44d3bc522e7964b76216a63a29b1c73400fcc0e71ee8/bio-1.3.3-py3-none-any.whl")
	version("1.3.4", sha256="cee6d82363d6c50432c1e917824e6f06bedb1a14f52d3ed20d837f9c893fdf61", expand=False, url="https://files.pythonhosted.org/packages/ab/7c/7c22fc20f8e79938bdba7d1de78b9bb55e1949d267d7270e09978203860b/bio-1.3.4-py3-none-any.whl")
	version("1.3.5", sha256="ef5262156aac261f794175f66fe6691ec8ae873a3fc4167deaf6feba0a45c2d0", expand=False, url="https://files.pythonhosted.org/packages/80/f2/97d9402620589248dea2a1445297314613181054f8be2719041ac1a90032/bio-1.3.5-py3-none-any.whl")
	version("1.3.6", sha256="21aab2a230bef6c3f17ca63a917c2b6c3cd6567fe180cf8d6f669b64f3ec97c7", expand=False, url="https://files.pythonhosted.org/packages/08/1e/3174419344e6c0dbb9731109b5af1e32f64e12ceabdf2ecc6b076bc9693e/bio-1.3.6-py3-none-any.whl")
	version("1.3.7", sha256="a67c9195fe6df20cd8dc40803774bed27081defa9a3a468032e96bc2728dbe06", expand=False, url="https://files.pythonhosted.org/packages/d0/33/d3459756d08609946cc4c44b10a789ff757010def6d88c182d772fc0793c/bio-1.3.7-py3-none-any.whl")
	version("1.3.8", sha256="e8bbf462635e395fc209abd720c71c887f7f8cb83732175f1ffc9b122a989ae0", expand=False, url="https://files.pythonhosted.org/packages/9a/34/2c993e035c518e2364b4adb6bad65c562e35add92257d4164a1d3451cf40/bio-1.3.8-py3-none-any.whl")
	version("1.3.9", sha256="dbcb40c53e00140d8b0139f7c58e5bf046cdf3258496b32fe8e07bd2bf2adf92", expand=False, url="https://files.pythonhosted.org/packages/86/dc/9a64aa1ead660a010c45101a5265d42dbfb159b7fec7ddba71a3dbaf7923/bio-1.3.9-py3-none-any.whl")
	version("1.4.0", sha256="23ba604790b5df151b9f070ced3bc7fec730bbf81953973cfa71744caf444aaa", expand=False, url="https://files.pythonhosted.org/packages/59/38/b31191b2845bc2cfbffec62be3376a2479cce424f49359ba69b78e892a58/bio-1.4.0-py3-none-any.whl")
	version("1.5.0", sha256="93ba7879576320ddd00c6cd56f0dd240a951f7b4acc2c9fb9bf4d07fa90626ae", expand=False, url="https://files.pythonhosted.org/packages/76/85/da9201d45a3158a91c6211d941faad134879929fd927f730631412a5d58e/bio-1.5.0-py3-none-any.whl")
	version("1.5.1", sha256="43be78a2aa7b1d7043aa21c17787858572649a09bc8d8542dc6378183399a9df", expand=False, url="https://files.pythonhosted.org/packages/25/15/257754f92979ca8504ba33db926744a5aceb683e37be82699cc455b0ef20/bio-1.5.1-py3-none-any.whl")
	version("1.5.2", sha256="e4359dede1fbb789cd303b29d6f14f5950a33447e68ee094bd42b57d26f0a3e0", expand=False, url="https://files.pythonhosted.org/packages/64/41/3ed9643c2566c2957964a45bd50e8eadfbda2ede83053ce80459c6a9bc8e/bio-1.5.2-py3-none-any.whl")
	version("1.5.3", sha256="6801fafb3673cb18d6920ed3e6b328b9c61cd9ee1fdc51ab9d91636b84c30567", expand=False, url="https://files.pythonhosted.org/packages/ae/6f/13eadabd2f920416a64a737e0e4fe8dc5326bfdae6a77b70dccd99b8013d/bio-1.5.3-py3-none-any.whl")
	version("1.5.4", sha256="58302dd58ffe5352bbbd29e2e15cc3ccc4f9df72865a7b5beb03ea72bb14b3bb", expand=False, url="https://files.pythonhosted.org/packages/0a/40/a6f5832d8791bf24ee461001bd576e4be995d134b8139de23b7fdc5d59c5/bio-1.5.4-py3-none-any.whl")
	version("1.5.5", sha256="1ff87c0abd1040e569c699024cb045f223e1a68b7c88ab59b33367f3b0c3160c", expand=False, url="https://files.pythonhosted.org/packages/3f/5b/70739eae20f207b14a767af627dbabc446793a94c1c3859e7b6a94652040/bio-1.5.5-py3-none-any.whl")
	version("1.5.6", sha256="98d4667625f6c84e3632bb77753358f1a462e75a7b2e7671b50e555a961dace4", expand=False, url="https://files.pythonhosted.org/packages/48/f7/907aefdebf7319afbec48892760ace3431e54c199c75c869c99129b34bff/bio-1.5.6-py3-none-any.whl")
	version("1.5.8", sha256="e5cef331756159ad83cbafd2181423498ba4cf6c8a2c288a581fccbeb1fb4857", expand=False, url="https://files.pythonhosted.org/packages/2b/6b/01c1715378e9c888f5eb7b5eae8f5757b04676d62df9fdf5b2072ff321e9/bio-1.5.8-py3-none-any.whl")
	version("1.5.9", sha256="b1c44e509922955a5d87de215f7d373796b278741735d86ce5663965d5cf386b", expand=False, url="https://files.pythonhosted.org/packages/79/ab/ad10761bdf295a5f2bfdc2734ed61d3c82aa570f0b679428dbe2caa2727c/bio-1.5.9-py3-none-any.whl")
	version("1.6.0", sha256="38b14e11625ef233e1a3878c8b13253695e863bd997f94715c248b71612605d5", expand=False, url="https://files.pythonhosted.org/packages/34/bd/5077f1d9f5a9508edae77a9647228a7304457d22469b2fe88ec7c990f10f/bio-1.6.0-py3-none-any.whl")
	version("1.6.1", sha256="e7dc23849283e35b6cfcf087314c08a53b942898f8b58e670b0c0a827d38fccb", expand=False, url="https://files.pythonhosted.org/packages/11/34/58672f9ba1b18d92b973b80cc711c4a35f5e2d4709be962a9043a33cc8c3/bio-1.6.1-py3-none-any.whl")
	version("1.6.2", sha256="dcec8207f3993a7f41bd8205cde235218da3dc008175ae7bb7468276d8dacf71", expand=False, url="https://files.pythonhosted.org/packages/c1/1e/6c4808999f33f63ed1327c6463d03f1209b08634183a237d9112370071b4/bio-1.6.2-py3-none-any.whl")
	version("1.7.1", sha256="851545804b08413a3f27fd5131edefc30acfdee513919eebabb29678d8632218", expand=False, url="https://files.pythonhosted.org/packages/cb/40/747f3038ac636e520da52f7b9f5721779a50f88fdfc165847b0d8127dae2/bio-1.7.1-py3-none-any.whl")
	version("1.8.0", sha256="8861fb3ef608d3ce8b2fd8dc8d9a901c4d29b58b9fbd30b5059d089c608a6e13", expand=False, url="https://files.pythonhosted.org/packages/5c/9e/8c85998902ada23fce54bef8cb864a8e84302f275fc178ec65f75db80abe/bio-1.8.0-py3-none-any.whl")

	depends_on("py-setuptools", type=("build"))
	depends_on("python@3.7:", type=("build", "run"))
	depends_on("python@3.10:", type=("build", "run"), when"@1.5.4:")
	depends_on("py-biopython", type=("build", "run"))
	depends_on("py-gprofiler-official", type=("build", "run"))
	depends_on("py-mygene", type=("build", "run"))
	depends_on("py-pandas", type=("build", "run"))
	depends_on("py-pooch", type=("build", "run"))
	depends_on("py-requests", type=("build", "run"))
	depends_on("py-tqdm", type=("build", "run"))
