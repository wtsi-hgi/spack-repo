# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyGtfparse(PythonPackage):
	"""Parsing library for extracting data frames of genomic features from GTF files"""
	
	homepage = "https://github.com/openvax/gtfparse"
	pypi = "gtfparse/gtfparse-2.5.0-py3-none-any.whl" 

	version("0.0.1", sha256="9a6746d9a3668745e0e4bc2a0040de97500f751089c671d42aff9dcf6cb8a4d8")
	version("0.0.2", sha256="e56ab27ebbfcdd5ee51a83b94a46e3c2cf92c7efecfecc88ad92f0278e2d2e0b")
	version("0.0.3", sha256="5198adc0b53a259703b5b098f5a72fa8c891590f344ad00b7e56c28113b57be7")
	version("0.0.4", sha256="1d0c1d05294f7cd482354916dbaa14458694d4cf5b4f3b37ed48e0f2162f7f91")
	version("0.0.5", sha256="c883bf008a0c8f68661512b7fe2a88bc341949c47ee4046382c5944e25f1757e")
	version("0.0.6", sha256="4e169a4dfb3b5a4eb4350a864e8435d7f7961c704b6c45cb0f540132f4e1d37e")
	version("0.2.0", sha256="78dcb358165d11e0491611315f4cb23d0add8bf638bb8961baabe4d6ab8e70af")
	version("0.2.1", sha256="8bdca88d322911cdb4d2574ced251f23bc61b4e85e6513b0f29e7096116e7037")
	version("0.2.2", sha256="5e28bf43cbe19cc25557e972a3272e078b4e6d00e4a72c94bd12ceed4415c7fe")
	version("0.2.3", sha256="a0e03180718e55a69c409aa6f02070061790f70e240d72516250218fa0d6e311")
	version("0.2.4", sha256="ebf2cfe7db68913882054d665a45042cc441262a866da661100afd2a246350fa")
	version("0.3.0", sha256="e507ffef3bc0e123ece29cbebebaec9ebf7d408033b0d64b058e9dd00d1b2407")
	version("1.0.0", sha256="9b12a66285947946169cccddc28c5ce30eb2df18dae6a82f1e3ccf369bbb1084")
	version("1.0.1", sha256="1bc6b17e320ea8516c3cc42018a09b8aaede1769e3ec740d21c15a97550eb80e")
	version("1.0.2", sha256="d20d06947ec39192115e580053c41707d3727da1d32fdfaec7d3e2b2de359ae1")
	version("1.0.3", sha256="3b748c36eb716718608b005f91c2ef7dde0c6fc3d26129a14f2f59b7825d0b96")
	version("1.0.4", sha256="27c9ca5089c7c3b76b7794a89c6a1040c95ebc7dddfc7dbbaf63187385a52586")
	version("1.0.5", sha256="766dde6b47ec4f77acf24683378b948bae9491548d2966eea8e55f429dc6e62c")
	version("1.0.7", sha256="568d2c52d9d2594d785e06e46c8590f8596ffe597275d42bffda661c7aeddb78")
	version("1.1.0", sha256="fa17416fb1545d37e8b229dc91b0a675e197b02403cd6e22534384f8417a54ae")
	version("1.1.1", sha256="d17afb9881c8391ef73a90593afe34e71709e9f4683065726e64558100cdedc7")
	version("1.1.2", sha256="c7ce355e79c2b9f81d2c7da048c4d9d1516023fa1781212ebeefb21e470d5076")
	version("1.2.0", sha256="2f27aa2b87eb43d613edabf27f9c11147dc595c8683b440ac1d88e9acdb85873")
	version("1.2.1", sha256="559d4d36b0bd5d4494f925cab3c00cd969783ebb6408fa025df92663965834b8")
	version(
		"1.3.0",
		sha256="d957f18e5f70413f89a28ef83068c461b6407eb38fd30e99b8da3d69143527b1",
		url="https://files.pythonhosted.org/packages/f5/bb/f97d06b60f32e30b7ba25336f0886c24b13855d7ca8642200e4d70382a45/gtfparse-1.3.0.tar.gz",
	)
	version("2.0.1", sha256="c45439af58cb48120910bebe4625371d8fb5735f12a749e8933c9d6f2b1a558c")
	version("2.1.0", sha256="7af57445713a53cb830039df1631a95928a204cb30846bd07a955f60afaa8d47", expand=False, url="https://files.pythonhosted.org/packages/d7/f1/2bb211c807a0c3bc59c6e8e97a89a7901ef997ec90d09ecfd9185284255d/gtfparse-2.1.0-py3-none-any.whl")
	version("2.2.0", sha256="366e66d41d263ca7633f0decc697defcdea5d87079dbbf2ce74da106f0a23549", expand=False, url="https://files.pythonhosted.org/packages/1e/bf/a1fcfdd483ecd82816738260cf44b326b828af1eb893f56db524c64a011b/gtfparse-2.2.0-py3-none-any.whl")
	version("2.3.0", sha256="f4dee0590c389bcbd34c1a82e0a465e4c1b911e388d4bceda8a82a4feb65365b", expand=False, url="https://files.pythonhosted.org/packages/ca/22/b1aa5d365478e03d03fcded7b6e055fcbf157c570cb71537ce95c45efdd1/gtfparse-2.3.0-py3-none-any.whl")
	version("2.4.0", sha256="c834234c40f74c2924943573645e700cbe399ac45f4cff378fbb28d4b056ca24", expand=False, url="https://files.pythonhosted.org/packages/90/2a/84f3d03d3db4d4ecb132148dd49254ad7ef66d57a7c9029785e7526f3241/gtfparse-2.4.0-py3-none-any.whl")
	version("2.4.1", sha256="31ebc67d33264d0e37b9a67959614099c99e2a63df042f26ec5d81c72c11d249", expand=False, url="https://files.pythonhosted.org/packages/a5/97/ce29851eb198dad398c9657f3ad3e33b9f368775fd62784d03841835f3fc/gtfparse-2.4.1-py3-none-any.whl")
	version("2.5.0", sha256="ccc9e9e77b7bdd90dda0e41da864714cb40b6b0c64ecc1d8a131e11497357140", expand=False, url="https://files.pythonhosted.org/packages/b1/4b/0cb91cedef2b9e93f340166e8709587e3c36366fff4964973ff0d38908ba/gtfparse-2.5.0-py3-none-any.whl")

	depends_on("py-setuptools", type=("build"))
	depends_on("python@3.7:", type=("build", "run"))
	depends_on("py-polars", type=("build", "run"))
	depends_on("py-pyarrow", type=("build", "run"))

# {'polars<0.21.0,>=0.20.2': ['2.1.0', '2.2.0', '2.3.0', '2.4.0', '2.4.1', '2.5.0'], 'pyarrow<14.1.0,>=14.0.2': ['2.1.0', '2.2.0', '2.3.0', '2.4.0', '2.4.1', '2.5.0']}
