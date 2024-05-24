# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyBranca(PythonPackage):
	"""Generate complex HTML+JS pages with Python"""
	
	homepage = "https://github.com/python-visualization/branca"
	pypi = "branca/branca-0.7.2-py3-none-any.whl" 

	version("0.1.1", sha256="7c378fc758b673fdfb21f0e2720ee221ff617fc146539a75a54dac29e9fd514e", expand=False, url="https://files.pythonhosted.org/packages/c7/e0/7e9151d121eb39d2b84953c4c2e8f01cc74943eb91008e596757cbde8383/branca-0.1.1-py3-none-any.whl")
	version("0.2.0", sha256="788aa8b6cbd387eb4a5b7fbd557743692d5ce559d02a6514ccfc384a04cb1ba0", expand=False, url="https://files.pythonhosted.org/packages/c3/fe/c140768eaf9d14ef6e844d0e9679b7085d87ceeaa578020fd6fed679d74c/branca-0.2.0-py3-none-any.whl")
	version("0.3.0", sha256="01737edb54a0acb7a959bde57bfad468a4541a3e5ff1be82b97c47fca619c612", expand=False, url="https://files.pythonhosted.org/packages/b5/18/13c018655f722896f25791f1db687db5671bd79285e05b3dd8c309b36414/branca-0.3.0-py3-none-any.whl")
	version("0.3.1", sha256="4d89048add9628d1f83a73c6482c116f6752580cc03d5fe09de0bdeb8e5a2158", expand=False, url="https://files.pythonhosted.org/packages/63/36/1c93318e9653f4e414a2e0c3b98fc898b4970e939afeedeee6075dd3b703/branca-0.3.1-py3-none-any.whl")
	version("0.4.0", sha256="5053265c8092963767ecfabd48dc524b94f4d6847beabe11f0fcb9d068fe55ba", expand=False, url="https://files.pythonhosted.org/packages/81/6d/31c83485189a2521a75b4130f1fee5364f772a0375f81afff619004e5237/branca-0.4.0-py3-none-any.whl")
	version("0.4.1", sha256="84eb4a2cc2c6f988c7ed07523de18c9867baeac3539a24cb3b66c255399bb1c5", expand=False, url="https://files.pythonhosted.org/packages/13/fb/9eacc24ba3216510c6b59a4ea1cd53d87f25ba76237d7f4393abeaf4c94e/branca-0.4.1-py3-none-any.whl")
	version("0.4.2", sha256="62c2e777f074fc1830cd40ba9e650beb941861075980babafead8d97856b1a4b", expand=False, url="https://files.pythonhosted.org/packages/61/1f/570b0615c452265d57e4114e633231d6cd9b9d275256778a675681e4f711/branca-0.4.2-py3-none-any.whl")
	version("0.5.0", sha256="781ff32bf82979584b0004bd84c254cfccda26bc31b2f7333346d03fb7b97741", expand=False, url="https://files.pythonhosted.org/packages/6c/e2/16ce27dbfbc48b460e95aa2e900e905d3f1069b89d992820234d41f0db95/branca-0.5.0-py3-none-any.whl")
	version("0.6.0", sha256="ae706fc7a88dd0296a58bb11c0cb3c6be358491a3b0abee08fe16b4db17814c0", expand=False, url="https://files.pythonhosted.org/packages/a6/18/cea6374623d82efc292996997cee0a13ae99359c7e66db22f92dc8484dd1/branca-0.6.0-py3-none-any.whl")
	version("0.7.0", sha256="c653d9a3fef1e6cd203757c77d3eb44810f11998506451f9a27d52b983500c16", expand=False, url="https://files.pythonhosted.org/packages/2f/e7/603b136221de923055716d23e3047da71f92e0d8ba2c4517ce49a54fe768/branca-0.7.0-py3-none-any.whl")
	version("0.7.1", sha256="70515944ed2d1ed2784c552508df58037ca19402a8a1069d57f9113e3e012f51", expand=False, url="https://files.pythonhosted.org/packages/17/ce/14166d0e273d12065516625fb02426350298e7b4ba59198b5fe454b46202/branca-0.7.1-py3-none-any.whl")
	version("0.7.2", sha256="853a359c34d08fd06498be762d8be9932750db4049cac11e25dd6f23562e25c2", expand=False, url="https://files.pythonhosted.org/packages/75/ca/6074ab4a04dd1a503201c18091b3426f3709670115fae316907a97f98d75/branca-0.7.2-py3-none-any.whl")

	depends_on("python@3.7:", type=("build", "run"))
	depends_on("py-jinja2", type=("build", "run"))
