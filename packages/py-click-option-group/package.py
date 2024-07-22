# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyClickOptionGroup(PythonPackage):
	"""Option groups missing in Click"""
	
	homepage = "https://github.com/click-contrib/click-option-group"
	pypi = "click-option-group/click_option_group-0.5.6-py3-none-any.whl" 

	version("0.1.0", sha256="6f7262d68345e90b897a9e24453650694114f0582af560832ee0bc81bd89c873", expand=False, url="https://files.pythonhosted.org/packages/0c/b5/0165f183681122ce085fbb3054c086b8ef4c1913347a9027fdbe9aa224ae/click_option_group-0.1.0-py3-none-any.whl")
	version("0.2.0", sha256="bb494b21f811ff293a9a28f3ef395e6a542ba60435e191200bf6712496f213cf", expand=False, url="https://files.pythonhosted.org/packages/ee/ba/9941f1d37bc3b9ece55ba7d924d1a68157ae3002016d420066b7b34dba8e/click_option_group-0.2.0-py3-none-any.whl")
	version("0.2.1", sha256="42a7184adce12629f432bca2b6e0b3633fc21fca3d7b66966e9df6cb10f32e50", expand=False, url="https://files.pythonhosted.org/packages/88/e1/faaa9e0923beec55eaee03484dd86f4724ea2cab07c2402952ff391e4663/click_option_group-0.2.1-py3-none-any.whl")
	version("0.2.2", sha256="d13beee55ee73161b5d8811b75c55665128f0d82f2c8381dd144161945955238", expand=False, url="https://files.pythonhosted.org/packages/8e/04/e77a40f0f2605fd7c5e46e5f8c96eb1b118b670a845b9c56bf3705a27e3c/click_option_group-0.2.2-py3-none-any.whl")
	version("0.2.3", sha256="984bce9c06fecff751178e6b2216b993c06874544f8cb1708e922b8591498e75", expand=False, url="https://files.pythonhosted.org/packages/f9/4b/4151219da4eb7baa31b469f640db938e5c5cd7650da0a2d5ffc1cdddeefa/click_option_group-0.2.3-py3-none-any.whl")
	version("0.3.0", sha256="e5dab79e3be37ede08962946cc87804501c442a6106579b6a743474269603add", expand=False, url="https://files.pythonhosted.org/packages/75/fc/86fe8cbd867896aa9db5b4ae659c5fea43abfa00fab2ae2b42fc92af9228/click_option_group-0.3.0-py3-none-any.whl")
	version("0.3.1", sha256="ca78d8adc11e411729b312321e359bb072f8a88c99249c6c71348f62133fb57f", expand=False, url="https://files.pythonhosted.org/packages/dd/7c/f1e9a5ba5ac3a1c6e0c0563e97b5c0c7bed1a54c187ee43a6edae3d99daa/click_option_group-0.3.1-py3-none-any.whl")
	version("0.4.0", sha256="6f1efaf1c587590eff849adbe1f633c4402598eafe0082d364479cba732003cf", expand=False, url="https://files.pythonhosted.org/packages/67/79/f5c781d979e01789ce626877044ca22e96fc11bffe260129c5f70313a424/click_option_group-0.4.0-py3-none-any.whl")
	version("0.5.0", sha256="e5bdea3ffa7009104e14bcce43feb46ae5b0132d7b9a167641566830e2c289bc", expand=False, url="https://files.pythonhosted.org/packages/bc/f0/7e670df7f9c8e492e3af08fbfeedb6687b50c67205de70b1e417a199e35c/click_option_group-0.5.0-py3-none-any.whl")
	version("0.5.1", sha256="b363552b81f3bc9bef2402837b08865d186bd97c2311768f7d52aaf896e384a6", expand=False, url="https://files.pythonhosted.org/packages/30/e9/1b3d4e54586f350c39f1d2077c5dfd3bc42138b5b80ded4a62462442064c/click_option_group-0.5.1-py3-none-any.whl")
	version("0.5.2", sha256="1b4b2ecf87ba8dea78060cffd294b38eea5af81f28a5f9be223c01b8c5ea9ab0", expand=False, url="https://files.pythonhosted.org/packages/8a/28/8c81b5b7ef0b831dac1bc23f807e264a38b3bcfb1280f7cf5dedf18b6651/click_option_group-0.5.2-py3-none-any.whl")
	version("0.5.3", sha256="9653a2297357335d7325a1827e71ac1245d91c97d959346a7decabd4a52d5354", expand=False, url="https://files.pythonhosted.org/packages/6f/87/88c4909488caca67c0fe435912efa7904955e6f36fc73106d56334252a94/click_option_group-0.5.3-py3-none-any.whl")
	version("0.5.4", sha256="0976f0dd15ab5f9f2ee0823f4b83c5a84f8748668c0c37a334739b287711940d", expand=False, url="https://files.pythonhosted.org/packages/36/84/06316d5fc1c5fa011b293effae02303bc616d5a7c93d4c68e88c027124fc/click_option_group-0.5.4-py3-none-any.whl")
	version("0.5.5", sha256="0f8ca79bc9b1d6fcaafdbe194b17ba1a2dde44ddf19087235c3efed2ad288143", expand=False, url="https://files.pythonhosted.org/packages/cf/b2/808e028b944a1f7c21005205762ee88654c40b73b9de2a04e18384d1c9cd/click_option_group-0.5.5-py3-none-any.whl")
	version("0.5.6", sha256="38a26d963ee3ad93332ddf782f9259c5bdfe405e73408d943ef5e7d0c3767ec7", expand=False, url="https://files.pythonhosted.org/packages/af/75/81ea958bc0f7e410257cb2a42531b93a7695a31930cde87192c010a52c50/click_option_group-0.5.6-py3-none-any.whl")

	depends_on("python@3.6:4", type=("build", "run"))
	depends_on("py-click", type=("build", "run"))

# {'Click(<8,>=7.0)': ['0.1.0', '0.2.0', '0.2.1', '0.2.2', '0.2.3', '0.3.0', '0.3.1', '0.4.0', '0.5.0', '0.5.1', '0.5.2'], "sphinx(>=2.3);extra=='docs'": ['0.3.0', '0.3.1'], "Pallets-Sphinx-Themes;extra=='docs'": ['0.3.0', '0.3.1', '0.4.0', '0.5.0', '0.5.1', '0.5.2', '0.5.3', '0.5.4', '0.5.5', '0.5.6'], "m2r;extra=='docs'": ['0.3.0', '0.3.1', '0.4.0', '0.5.0', '0.5.1', '0.5.2', '0.5.3'], "pytest;extra=='tests'": ['0.3.0', '0.3.1', '0.4.0', '0.5.0', '0.5.1', '0.5.2', '0.5.3', '0.5.4', '0.5.5', '0.5.6'], "sphinx(<3,>=2.3);extra=='docs'": ['0.4.0', '0.5.0', '0.5.1', '0.5.2', '0.5.3'], "coverage(<6);extra=='tests'": ['0.4.0', '0.5.0', '0.5.1', '0.5.2', '0.5.3', '0.5.4'], "pytest-cov;extra=='tests'": ['0.4.0', '0.5.0', '0.5.1', '0.5.2', '0.5.3', '0.5.4'], "coveralls;extra=='tests'": ['0.4.0', '0.5.0', '0.5.1', '0.5.2', '0.5.3', '0.5.4'], 'Click(<9,>=7.0)': ['0.5.3', '0.5.4', '0.5.5', '0.5.6'], "sphinx(<6,>=3.0);extra=='docs'": ['0.5.4', '0.5.5'], "m2r2;extra=='docs'": ['0.5.4', '0.5.5', '0.5.6'], "pytest;extra=='tests_cov'": ['0.5.5', '0.5.6'], "pytest-cov;extra=='tests_cov'": ['0.5.5', '0.5.6'], "coverage(<6);extra=='tests_cov'": ['0.5.5'], "coveralls;extra=='tests_cov'": ['0.5.5', '0.5.6'], "sphinx;extra=='docs'": ['0.5.6'], "coverage;extra=='tests_cov'": ['0.5.6']}