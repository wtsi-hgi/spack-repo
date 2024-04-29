# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyScprep(PythonPackage):
	"""scprep"""
	
	homepage = "https://github.com/KrishnaswamyLab/scprep"
	pypi = "scprep/scprep-1.2.3-py3-none-any.whl" 

	version("0.1.0", sha256="6d4df64b0eaaa733683db4e436a37af6edc64b2990bb380d6589b366597b8f05")
	version("0.10.0", sha256="7071d8996fa0953294515faa663d275040b78eb6c966dda4acdfaa3bd9ca08d6", expand=False, url="https://files.pythonhosted.org/packages/10/c5/39a3320daa76ca4a93acab4bd792dd0e3de3dec3786156a49f4ef6eccec3/scprep-0.10.0-py3-none-any.whl")
	version("0.10.1", sha256="72ee980a930b7e1b7a149f3e7e53786bd16d32e5a6505ec03effd316398fbb15", expand=False, url="https://files.pythonhosted.org/packages/02/44/3766c19ab827cda07d5c8a2fa3a9cf28140b0cbdeda1beeffa5d8cefa615/scprep-0.10.1-py3-none-any.whl")
	version("0.10.2", sha256="147d18f3e6bbc894c8de11e040d8fa004a0170067b4173a05be089f30a24dad2", expand=False, url="https://files.pythonhosted.org/packages/c9/99/a798ce81c31781a32bc8b728a6c8e09837c7e9ea9207a647873ab743c06c/scprep-0.10.2-py3-none-any.whl")
	version("0.11.0", sha256="7ce2215cd4c6ff33d2ee5b9bd4d03a7018eea9a534992e2bafc39063bf831e4d", expand=False, url="https://files.pythonhosted.org/packages/82/dc/5f78a55fb00be61390e004f23893c4d970c63a365836f794e8f082f59394/scprep-0.11.0-py3-none-any.whl")
	version("0.11.1", sha256="d9acbef84d5b43b929c668e4dced98e7615794c76c37459ba626074be6c3d3b1", expand=False, url="https://files.pythonhosted.org/packages/f6/5e/4e260be4486eba9f612ae270bd2c17e9fca19a780433858023142d1057e1/scprep-0.11.1-py3-none-any.whl")
	version("0.12.0", sha256="6887a9bc0f753b7d59825ad44ee803ac2956df34f81142ff9d2c17b16bedbf63", expand=False, url="https://files.pythonhosted.org/packages/ce/37/01e8b03c361b87980fed1d43d9d84a4e338dab5bb7d0a4b339184efaf5b2/scprep-0.12.0-py3-none-any.whl")
	version("0.12.1", sha256="596212b8a302389361762f2cb66f17462d41afcb4354cb594c12c5abefc7e0be", expand=False, url="https://files.pythonhosted.org/packages/f8/0e/4ba3579d092e33cf47eb618118ee71c577a4e232b4cf047357010a7bda83/scprep-0.12.1-py3-none-any.whl")
	version("0.12.2", sha256="ea3e5dd6e0f040b1e55adeefcc999478c62ce1a3ebbdf9f1f613213d71a862b7", expand=False, url="https://files.pythonhosted.org/packages/14/e4/c90d0b917704f3729c1ca1f3ec831df97124528428ec85ccf023cab9fad1/scprep-0.12.2-py3-none-any.whl")
	version("0.2.0", sha256="41cc1330fcf7cbb2e0cf3dc3a7f0b235be85f91d8ff19ff78f812d87eb74bdd7")
	version("0.2.1", sha256="fbb1039b4100818b24a2b47ac7d347b015637e16167106648a1544dc17ee6d45")
	version("0.3.0", sha256="5c977760dfc2c6ffbb9e4b7f5239a26db60e31f0511e6b79b2cae97987662c75")
	version("0.3.1", sha256="1236222419b0ae84cf8bdead0dc1144e145731795cb859caef86cee58aa1249e")
	version("0.4.0", sha256="2ee78a0aa37bf0371904d27faa25ea0c3333877a2ede76f16fb7d16be43a0990")
	version("0.5.0", sha256="2112495c6a4b80e0381d0a2732da7f00b5aed823c8bbe8a49ce4f93c202fb44c")
	version("0.6.0", sha256="b80a6a8907c18598f4c4f99be888baa9d58c4782992bb07922b8dec06762c725")
	version("0.6.1", sha256="6d576782e61264009056ccff781c423480f27c929d8bc85f2ee63e179f64e8d7")
	version("0.6.2", sha256="5402bed16a5fc617ad85f9c8797812ed77cd55973ec00e3cd3728756dddca927")
	version("0.7.0", sha256="6e0d1b7b8106d9ac122076ac553dfa54e7c7590cc0d15005834e1f05f357d2ff")
	version("0.7.1", sha256="916f21dbda25f085378c5e44d28cfc4bd91ccedbbdc09b77d15cb81e31e18fe3")
	version("0.8.0", sha256="6676d66f3ef0e85ce8257b1d85b28f6dd4e13927447ce56fd611126aafaff6fe", expand=False, url="https://files.pythonhosted.org/packages/48/48/75f1a87f21dcc930e75befa2ea3aec981c5155ece09854a69a4f62026d40/scprep-0.8.0-py3-none-any.whl")
	version("0.8.1", sha256="a66b8f6b767b02d8246c06f8c3ed42d8588c9479e0e5997509e399c7c3173230", expand=False, url="https://files.pythonhosted.org/packages/9d/31/6ef4119b331b881ae6e6f76f115db3cb82e2d4ee97966d356f7dda931191/scprep-0.8.1-py3-none-any.whl")
	version("0.9.0", sha256="ced5edc7133489548c2c3a55423a06783c541c01acee8ba3b58b34c0805a65b5", expand=False, url="https://files.pythonhosted.org/packages/df/ab/a01a940191af774aec1eb041e6b4bca0c9d5d21c50a6cf1806d6ef294bbe/scprep-0.9.0-py3-none-any.whl")
	version("1.0.0", sha256="f8501576d1300bbc6744b9ddce8a1ca4484db632c07c2b544a35234e169c4b3d", expand=False, url="https://files.pythonhosted.org/packages/0f/38/43515a3b50a8bbbadc2b07c2f652ef4fc2372c5ce09121c10b98e0351682/scprep-1.0.0-py3-none-any.whl")
	version("1.0.1", sha256="3826f4243285a041f5740b8292d885abc24cdb21ebcbcc0107a8b02cc3a75562", expand=False, url="https://files.pythonhosted.org/packages/6a/b9/c6f36e23284bdd30a8ba0ac2475e244bdf81ffa19346beacc9b631aa3f90/scprep-1.0.1-py3-none-any.whl")
	version("1.0.10", sha256="adfd2c7e5e28f0de9fc020dbe0be1ed6f7fd17c7d2f40759cbac3e6ad042eb75", expand=False, url="https://files.pythonhosted.org/packages/de/62/071836b341c158c164609ccc2b6a8d59afc650ec0b561aa5b32d6f36fc55/scprep-1.0.10-py3-none-any.whl")
	version("1.0.11", sha256="b897d1c9b8995141db717da4687bd648d0959cfada9cf32fd4164cf6ab7a7bf5", expand=False, url="https://files.pythonhosted.org/packages/17/41/f2d4728a5c4d762b5e7424e80fd6297ad53c58bc666d1cc8236827462b8c/scprep-1.0.11-py3-none-any.whl")
	version("1.0.12", sha256="614274400e7444739ee45a9000dfae4c3ed61f4f1e5cda5110252658aa9642a8", expand=False, url="https://files.pythonhosted.org/packages/67/9f/883779ec2aadef51559f8a1ee039a6f5af3b5c12d1144d0890b241b7085e/scprep-1.0.12-py3-none-any.whl")
	version("1.0.13", sha256="238c03667ddcdf64b026d76b2f1bbb43de0ce5956529df89e836061cb960abd0", expand=False, url="https://files.pythonhosted.org/packages/34/50/22d102aa295556f508b24fd8149c05207cf093e082a2c0eab2d3d7c00978/scprep-1.0.13-py3-none-any.whl")
	version("1.0.2", sha256="8b5d554621f86156e3b4574bf85da30e9d3b90786843948902b1f213cc98dfad", expand=False, url="https://files.pythonhosted.org/packages/17/f4/8ea727d508c7473b9852138655199091a3701851706898fdc6ec7af88ae9/scprep-1.0.2-py3-none-any.whl")
	version("1.0.3", sha256="037449e180037fb9a00aa3aa33d7d2181bd7e1a8fbf8b25b5d46b2b8707774e3", expand=False, url="https://files.pythonhosted.org/packages/c6/b3/e039c5181e50aa0cc9057639f100ab50483f6dfb67b602bcffe1093c1ae4/scprep-1.0.3-py3-none-any.whl")
	version("1.0.4", sha256="d8c08fb47479892fa342a398296e93ca382b755c6467db2588f3745be7e36658", expand=False, url="https://files.pythonhosted.org/packages/74/24/242b0903bf0dbfb2e9e6245317ef5597f5b7252684826a6a9100adcfbb8e/scprep-1.0.4-py3-none-any.whl")
	version("1.0.5", sha256="23a713b29bd195ab6f8e9c9b1aeb5160068cd67aa45c588ff7956959ffbb64d6", expand=False, url="https://files.pythonhosted.org/packages/18/d2/01af6c4e574368bdccbc6e10625c19971186712c3453a3398f6ef2cfdb05/scprep-1.0.5-py3-none-any.whl")
	version("1.0.5.post2", sha256="1a1b689359f343683be29a797d237c1d4e82ce7cf32e7547fc2f94a265e02f9f", expand=False, url="https://files.pythonhosted.org/packages/73/38/0a4fe0cd17dd0b7e859718a769b1e799467098709b80b96175f43b098ca6/scprep-1.0.5.post2-py3-none-any.whl")
	version("1.0.6", sha256="ef155660baf6a970df04d057040d93963c35ee5080a8cd4b0179086b1c76e856", expand=False, url="https://files.pythonhosted.org/packages/7c/88/e831f0d79243d43e1fc3978f91e7eace5a4c872e7366be675808465dc81f/scprep-1.0.6-py3-none-any.whl")
	version("1.0.7", sha256="acd90d984f6ef8586b15569fcd66da4f54b78e102e771ddee805424e6d01ebd6", expand=False, url="https://files.pythonhosted.org/packages/36/5d/29523734ecbfc0960699b046341a3f07e4bda5f91bf2dc062f1c5846c1ab/scprep-1.0.7-py3-none-any.whl")
	version("1.0.8", sha256="0061ea0e891afec90cfd41101fa3c2c98b75cdbfddfdc286c6201c2a52fac0ea", expand=False, url="https://files.pythonhosted.org/packages/15/e2/2aa1625e4ccc848879267d95e207c1f4d2fbcd5bec2fa84ca50933c8e3aa/scprep-1.0.8-py3-none-any.whl")
	version("1.0.9", sha256="414371122531fdae5d925ae717e9b4a5ba3d2a0a39e1fd5d28add93aaf92be57", expand=False, url="https://files.pythonhosted.org/packages/e4/6c/d2761b02f50f2c050f6c56f4b737d8f599d374c784e325b83a15f063890d/scprep-1.0.9-py3-none-any.whl")
	version("1.1.0", sha256="338af5565321d3b54a15a7635e5bc5160f84569bb889e1c369d4c3b3afecdc40", expand=False, url="https://files.pythonhosted.org/packages/92/91/dfb35608ffae7eb0f45b565e702d3083d784988200ab6a967fd3f60d833e/scprep-1.1.0-py3-none-any.whl")
	version("1.2.0", sha256="6763b00c819e0e793dad0ac8d3b69cac0f8353cc4ae7282463041e58f0c8b94f", expand=False, url="https://files.pythonhosted.org/packages/76/c4/ca11391341e30292cd1f79c29ff3e6908a3ea4c03cb4bb73d20fa0e507b3/scprep-1.2.0-py3-none-any.whl")
	version("1.2.1", sha256="49880ad5efb5cac1f1ad6f250d2aa0f0b413088731838155fec4e90fd6fd49e0", expand=False, url="https://files.pythonhosted.org/packages/48/ae/d1cddfb18957493f1b39206b1fda97be1ee85766bf3e9fb1914c90b6879f/scprep-1.2.1-py3-none-any.whl")
	version("1.2.2", sha256="2546cd1093d23a532dcb6c3a9b4ec3c8e5e9a8ddbcce77936ebb6882a90065f5", expand=False, url="https://files.pythonhosted.org/packages/4d/31/fff89359a73ec252b9c59df2a14e528435cd44793a3425ad60f32d8dea06/scprep-1.2.2-py3-none-any.whl")
	version("1.2.3", sha256="31c75956baee3fc7a079957ce4e01821b36012163bd9d34e48afc74b42b5d875", expand=False, url="https://files.pythonhosted.org/packages/2a/d2/72a06c97668b07ef703ffdc392cbd5ce004733d14978f6ae2ae71a09df41/scprep-1.2.3-py3-none-any.whl")

	depends_on("python@3.6:", type=("build", "run"))
	depends_on("py-packaging", type=("build", "run"))
	depends_on("py-pandas", type=("build", "run"))
	depends_on("py-decorator", type=("build", "run"))
	depends_on("py-scikit-learn", type=("build", "run"))
	depends_on("py-scipy", type=("build", "run"))
	depends_on("py-numpy", type=("build", "run"))
