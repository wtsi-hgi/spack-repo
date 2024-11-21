# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PySpatialImage(PythonPackage):
	"""spatial-image"""
	
	homepage = "https://github.com/spatial-image/spatial-image"
	pypi = "spatial-image/spatial_image-1.1.0-py3-none-any.whl" 

	version("0.0.1", sha256="6016e0cd5be0b86e63b46463eb02a7c0ec7c0519c19d3d57d32cad2a0838bef8", expand=False, url="https://files.pythonhosted.org/packages/29/7b/7626bb4070fcd31965e184e8f7ac42ce751c4b19adb8c6454c5b7dd05728/spatial_image-0.0.1-py2.py3-none-any.whl")
	version("0.0.2", sha256="bfdd1adfa09f536216b42564135bed4cb7a9641483980d48195b54f1c1f24552", expand=False, url="https://files.pythonhosted.org/packages/ad/58/a213c2ed7c0d26c32e13acd54c452d906cee1d5e65cd9a5c328c018f76c8/spatial_image-0.0.2-py2.py3-none-any.whl")
	version("0.0.3", sha256="a61c7749f594ffea4a44c1e1a2b21e9260e01b3b856e678e10906bf311acfe86", expand=False, url="https://files.pythonhosted.org/packages/4e/80/ad74c35260226adbb270782f1f0a264a5a8fc30826341a5c531ae55ccf2d/spatial_image-0.0.3-py2.py3-none-any.whl")
	version("0.1.0", sha256="490217fd2c16a222efcae67244a86ac2c3d369aed1b5f67802a5d098386f64f3", expand=False, url="https://files.pythonhosted.org/packages/8e/e5/09c1c34c18cc6867bf155ca276b17a8e9eb28ff8aa8d5719a37eba2d7154/spatial_image-0.1.0-py3-none-any.whl")
	version("0.2.0", sha256="4e3d73b87b26e599b85798342fd032ff3e04e6744c8e934286a0a9e24a9126f1", expand=False, url="https://files.pythonhosted.org/packages/fa/77/749be494b15ec1391d96a82832eb8e25d3892ec559e24fc1837f845ce05e/spatial_image-0.2.0-py3-none-any.whl")
	version("0.2.1", sha256="485bbd159a44057dba116faee733b9b4a58a018483aa45aa1456721e5cf42132", expand=False, url="https://files.pythonhosted.org/packages/d5/30/803cfc560a3f88e7859e1a083baca0d366757ba543542ac0e0f7b35aff4f/spatial_image-0.2.1-py3-none-any.whl")
	version("0.3.0", sha256="aa4bd9a6c538146c00ac7f27fa05cad1070174df8522f88db10e680622dd8211", expand=False, url="https://files.pythonhosted.org/packages/90/5b/00be212a4f52c2a49ec8c4fe7c3b4031fb6efa312dde2caabfd801ffd429/spatial_image-0.3.0-py3-none-any.whl")
	version("1.0.0", sha256="08efa442b5b8f46bffa6cad4ff046c77e375021655686904c33fd1065b2dfb30", expand=False, url="https://files.pythonhosted.org/packages/fb/99/c4f9f230ea083c195af0dc542331b76b4441516da7c32c33c3b4b51e96ba/spatial_image-1.0.0-py3-none-any.whl")
	version("1.1.0", sha256="f7f9b89e20ced35ee50efb588399d384d44c8242bee686a2e8add2fc9ab3ef56", expand=False, url="https://files.pythonhosted.org/packages/10/e5/134cfa437c0d87ce33b28b593a9990ceb4dd425e104c8da3efc299dccc55/spatial_image-1.1.0-py3-none-any.whl")

	depends_on("py-setuptools", type=("build"))
	depends_on("python@3.8:", type=("build", "run"))
	depends_on("py-numpy", type=("build", "run"))
	depends_on("py-xarray", type=("build", "run"))
	depends_on("py-xarray-dataclasses", type=("build", "run"))

# {'numpy': ['0.0.2', '0.0.3', '0.1.0', '0.2.0', '0.2.1', '0.3.0', '1.0.0', '1.1.0'], 'xarray': ['0.0.2', '0.0.3', '0.1.0', '0.2.0', '0.2.1', '0.3.0', '1.0.0', '1.1.0'], 'pytest;extra=="test"': ['0.0.2', '0.0.3', '0.1.0', '0.2.0', '0.2.1', '0.3.0', '1.0.0', '1.1.0'], 'pytest-mypy;extra=="test"': ['0.0.3', '0.1.0', '0.2.0', '0.2.1', '0.3.0', '1.0.0', '1.1.0'], 'xarray-dataclasses>=1.1.0': ['0.1.0', '0.2.0', '0.2.1', '0.3.0', '1.0.0', '1.1.0']}