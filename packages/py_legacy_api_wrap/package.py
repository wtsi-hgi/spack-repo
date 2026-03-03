# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyLegacyApiWrap(PythonPackage):
	"""Wrap legacy APIs in python projects"""
	
	homepage = "https://github.com/flying-sheep/legacy-api-wrap"
	pypi = "legacy-api-wrap/legacy_api_wrap-1.4-py3-none-any.whl" 

	version("0.1", sha256="e13ab280415ae862260e23478414f0578e3488e0dd073337b9766213304fbcfb", expand=False, url="https://files.pythonhosted.org/packages/25/b4/f9d61e817a897434a5ed32c9344d00b0d0f427a7e49a436eb52f0716a140/legacy_api_wrap-0.1-py2.py3-none-any.whl")
	version("1.0", sha256="629cc2e1b8bd73e998e13e196d80eb1dc679170166300b24aa70c732c35efa62", expand=False, url="https://files.pythonhosted.org/packages/3e/a5/4a0911195962cdacb0e36113118ba3f49fed94c352953edd1b11f1e6f4ef/legacy_api_wrap-1.0-py3-none-any.whl")
	version("1.1", sha256="1ba149887f07c5748eb8c793a0cab53ff16ce3cce1b4efe372fbd103e7c03826", expand=False, url="https://files.pythonhosted.org/packages/84/5f/c400f9094ea8c3ef83184126bea6f5cdfb19bdd0fe048c57a1d697e70f2c/legacy_api_wrap-1.1-py3-none-any.whl")
	version("1.2", sha256="f32cce6dd2f38d666b348c2b5ef8ecb724c23bdb648882eec64d0e0ee2ba9e24", expand=False, url="https://files.pythonhosted.org/packages/a4/68/da997bc56bb69dcdcee4054f0bc42266909307b905389fbc54c9158f42da/legacy_api_wrap-1.2-py3-none-any.whl")
	version("1.3", sha256="d22db26b7db2be3a83011d9f7efc7e09075ce5bee20556cd4daae47632f96978", expand=False, url="https://files.pythonhosted.org/packages/2f/9d/876a80e25965194e82278ebf531a2388ddb5c02f33f88f8f16952362b631/legacy_api_wrap-1.3-py3-none-any.whl")
	version("1.4", sha256="bf81b8ee432d80e7203aa079c26fc3a0f228d158db808868f10c2e36a8f64dbd", expand=False, url="https://files.pythonhosted.org/packages/97/08/eaf39f00542e4181b65617805f116a0d38daec98d0dce36ec94327ca8fc4/legacy_api_wrap-1.4-py3-none-any.whl")

	depends_on("python@3.8:", type=("build", "run"))

# {'get-version>=2.0.4': ['0.1', '1.0', '1.1', '1.2'], 'setuptools': ['0.1', '1.0', '1.1', '1.2'], 'future-fstrings': ['1.0', '1.1'], 'pytest;extra=="test"': ['1.0', '1.1', '1.2'], 'pytest-cov;extra=="test"': ['1.0', '1.1', '1.2'], 'pytest-black;extra=="test"and(python_version!="3.5")': ['1.0', '1.1', '1.2'], "coverage;extra=='test'": ['1.3', '1.4'], "coverage-rich;extra=='test'": ['1.3', '1.4'], "pytest;extra=='test'": ['1.3', '1.4'], "toml;extra=='test'": ['1.3', '1.4']}