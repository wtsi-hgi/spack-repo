# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPingouin(PythonPackage):
	"""Pingouin: statistical package for Python"""
	
	homepage = "https://pingouin-stats.org/index.html"
	pypi = "pingouin/pingouin-0.5.5-py3-none-any.whl" 

	version("0.1.0", sha256="82fb97ecd56b4ce6853411d9ad2d76a7603ef989b232a97fe36b13bf7ca69863")
	version("0.1.1", sha256="98e906591323ed328d3b3cbf5f59bdd06ff43d0b7c93ac3ee3c1c9622136e16f")
	version("0.1.10", sha256="74cc29a1dfbd71a50542bfbefbed586166e488a85ac0bd612da6070bdd82807b")
	version("0.1.2", sha256="2b0783982335d792144f0bae3abc5246548c380ff37958f3aaf97acc8f239646")
	version("0.1.3", sha256="23a3d155bd0949e596d18d6cd0b23bd56952cb41bd7dd3d981f35cf1065a41cb")
	version("0.1.4", sha256="ebec0c42c297e3170a0931c39fa6d622ddbe6779780449ecbbef547821d7c964")
	version("0.1.5", sha256="e14e962c4084658385ebe9e25acd9f8fc37aebf3ffd4a9cf940c848887611844")
	version("0.1.6", sha256="550698f3620f5ae4f0e2c7d8b2ae1518129965c084645def92ebb03d34f048a2")
	version("0.1.7", sha256="01f32f3be185f1776abd7ef719ca529c9c07a7ae3b5386daedb97bd11a651876")
	version("0.1.9", sha256="57b382a7e7a3276fc442fa1f01324b3c157dc003486fdb2c70f24247e0776529")
	version("0.1.dev0", sha256="ff3ed0461701e2d046fbf2c5da3c2d21288ac8d68b8512f35207b24344d7e81f")
	version("0.2.0", sha256="1fcf5469bc7d7c414803a8e01062019ef3be0182309206815663b514dd79842b")
	version("0.2.1", sha256="b1ee6f534d96484d9a3b201ca8a2a40f315d975918c1600868a4df23a500dd34")
	version("0.2.2", sha256="1f585181b7f6722d61b8b1155a0bddf1bdb6de7caecd2a78ba5ace7e32ecd13a")
	version("0.2.3", sha256="64d3d2ce220ab90fd6ff9b066b0d7b903bef6c2af400391ae586f09a66cc7de9")
	version("0.2.4", sha256="be8820555ba9a182eab354823b82bfd3ae926dcbc4115568470d6a4f1c4c46a0")
	version("0.2.5", sha256="ffa12405272045c4ea759c4667bcd9703e27877f822ee69490a872bc2748a65d")
	version("0.2.6", sha256="abbb3695ce55d1f0a3895e86dc653a8e54cf6262ff67105822c8b6d635d15b42")
	version("0.2.7", sha256="cfbae12df4a3fc52882af559f8a452291b0e93a1a8792790648858cc0b2bf89e")
	version("0.2.8", sha256="6714a2211a5dd2ca8470ba194102e3954de5a82961b32cb4035c918bbacd33a5")
	version("0.2.9", sha256="d11ac84ddd45240dcdcb4d6435faf45db7ef577de4ab12e26d5252b95fdc9474")
	version("0.3.0", sha256="1c0873879c79c721e9c3f8b81db52734c77e6568a4b9b01a3111b8b906f2b070")
	version("0.3.1", sha256="8fd35afd1c300e8dd78793773d71a51c50c112722539d7461aecb136da6d514e")
	version("0.3.10", sha256="68b734a8ba368bdf3d43ede99f9267ec4522d34786ad1ec840938f0df36add5f")
	version("0.3.11", sha256="91a636f3028f7a62402b884dccaff4b02ac1383f3d70148a0280f91157d53956")
	version("0.3.12", sha256="38e265394fe6a16de23a153a60d7d3db02c38427a31cc88c70523783cdc6c5ac")
	version("0.3.2", sha256="67715d3624757cc4c532989b3ed6d01f5e3b42c435f011282818f67dd7c22ddc")
	version("0.3.3", sha256="1637c5109de817e9b3cb03a9085f6eec35c555fc7e5b27e0940ea8f0fa73a93f")
	version("0.3.4", sha256="5af652c2e1c0ccef437bbabe18bafb6942a4968772d474bfc37c1cd438bde8e4")
	version("0.3.5", sha256="5322bd35e6c769fbddfc82a6112bd7411e63b2de8ff9312c238d79acea1e3514")
	version("0.3.6", sha256="19a002dfa1f7aac63827acdae1764e5aed14c9e450255a5341b5469a79f3d525")
	version("0.3.7", sha256="32f1cedce4b34d52b89465426a57e29b1da233a94e52d8a16aa0720b0cf94493")
	version("0.3.8", sha256="ae12581174740a358ca9127bdc2360edf7af357b094de682c80f993ff402b813")
	version("0.3.9", sha256="72a2cc3d7f97bb58da9ac3b69d6fd08e329c99309b29eb6ddd929d1159c61660")
	version("0.4.0", sha256="24249c4c98e4334736938ccb337f486b6a203206c68cfbee37b82c0f89c1ed88")
	version("0.5.0", sha256="343653303c471fb77edf9163e3c74caeb2e27baff0e145aacf708829ef4abf65")
	version("0.5.1", sha256="c00d40d6b46d780513d5a63d806347eafe89f68da882b0e6313cd392a91bd24e")
	version("0.5.2", sha256="00b8c8bc976b745bcc38a6c09dc5186e91da2b1b25006310641e8dd40a75369c")
	version("0.5.3", sha256="055fb0385ec9c426086e6a62bb1f5d7a7a8a1ed6ddc058c6f529a54f6316456b", expand=False, url="https://files.pythonhosted.org/packages/27/bd/ea43fb929d1f20f9059fd8539eab06f4e1a5325b59854a10c5d88f62e37e/pingouin-0.5.3-py3-none-any.whl")
	version("0.5.4", sha256="c3b1fdd2794b0f1b1d96a0fdc5d6d7207ead51b04083ae6c1f302e9ca4c7e408", expand=False, url="https://files.pythonhosted.org/packages/35/2e/8ca90e7edc93bc3d3bdf6daa6d5fc5ae4882994171c3db765365227e1d58/pingouin-0.5.4-py2.py3-none-any.whl")
	version("0.5.5", sha256="3156afe44ee5541131200848ee905937930757b615aca8eed8438ad4d4e20ef1", expand=False, url="https://files.pythonhosted.org/packages/eb/56/6d3607f3a78aee1de8e5466f5171722c8e344266a12dc44ccb73d024b3b3/pingouin-0.5.5-py3-none-any.whl")

	depends_on("python@3.8:", type=("build", "run"))
	depends_on("py-tabulate", type=("build", "run"))
	depends_on("py-statsmodels", type=("build", "run"))
	depends_on("py-seaborn", type=("build", "run"))
	depends_on("py-scipy", type=("build", "run"))
	depends_on("py-scikit-learn", type=("build", "run"))
	depends_on("py-pandas-flavor", type=("build", "run"))
	depends_on("py-pandas", type=("build", "run"))
	depends_on("py-numpy", type=("build", "run"))
	depends_on("py-matplotlib", type=("build", "run"))
	depends_on("py-mpmath", type=("build", "run"))

# {'numpy(>=1.19)': ['0.5.3'], 'scipy(>=1.7)': ['0.5.3'], 'pandas(>=1.0)': ['0.5.3'], 'matplotlib(>=3.0.2)': ['0.5.3'], 'seaborn(>=0.11)': ['0.5.3'], 'statsmodels(>=0.13)': ['0.5.3'], 'scikit-learn': ['0.5.3', '0.5.4'], 'pandas-flavor(>=0.2.0)': ['0.5.3'], 'outdated': ['0.5.3'], 'tabulate': ['0.5.3', '0.5.4', '0.5.5'], 'numpy': ['0.5.4', '0.5.5'], 'scipy': ['0.5.4', '0.5.5'], 'pandas(>=1.5)': ['0.5.4'], 'matplotlib': ['0.5.4', '0.5.5'], 'seaborn': ['0.5.4', '0.5.5'], 'statsmodels': ['0.5.4', '0.5.5'], 'pandas-flavor': ['0.5.4', '0.5.5'], 'pandas>=1.5': ['0.5.5'], 'scikit-learn>=1.2': ['0.5.5'], 'sphinx>7.0.0;extra=="docs"': ['0.5.5'], 'pydata-sphinx-theme;extra=="docs"': ['0.5.5'], 'numpydoc;extra=="docs"': ['0.5.5'], 'sphinx-copybutton;extra=="docs"': ['0.5.5'], 'sphinx-design;extra=="docs"': ['0.5.5'], 'sphinx-notfound-page;extra=="docs"': ['0.5.5'], 'pytest>=6;extra=="test"': ['0.5.5'], 'pytest-cov;extra=="test"': ['0.5.5'], 'codecov;extra=="test"': ['0.5.5'], 'openpyxl;extra=="test"': ['0.5.5'], 'mpmath;extra=="test"': ['0.5.5'], 'coverage[toml]>=5.3;extra=="test"': ['0.5.5']}