# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyXarraySchema(PythonPackage):
	"""Schema validation for Xarray objects"""
	
	homepage = "https://github.com/carbonplan/xarray-schema"
	pypi = "xarray-schema/xarray_schema-0.0.3-py3-none-any.whl" 

	version("0.0.1", sha256="eca2239445f353aaaa91b9550935bf946d01ce8f7df0a3713ef001501b2f9fe9", expand=False, url="https://files.pythonhosted.org/packages/9d/17/ca1cb2e13e1bef6fef975b8de8a698cb3507baed26c3b65771dbdfc0d7d1/xarray_schema-0.0.1-py3-none-any.whl")
	version("0.0.2", sha256="3b8e45bd7bf44216406b83e2871d1503e6c71ca497d07429c7aac51510a7c4e3", expand=False, url="https://files.pythonhosted.org/packages/11/17/a3aeaf19847a960a1f0dfa18186c65abb9353673c8fd8461ae25d44070ff/xarray_schema-0.0.2-py3-none-any.whl")
	version("0.0.3", sha256="aa6f856626b2e100213ba290407797464608b2555bb8e0b26093a97fe1ba38ce", expand=False, url="https://files.pythonhosted.org/packages/a9/6d/f585a27b380ee987619b5617c0ca672a71a4345b67cfedbb6299750ce845/xarray_schema-0.0.3-py3-none-any.whl")

	depends_on("py-setuptools", type=("build"))
	depends_on("python@3.8:", type=("build", "run"))
	depends_on("py-xarray", type=("build", "run"))
	depends_on("py-numpy", type=("build", "run"))

# {'xarray(>=0.16)': ['0.0.1', '0.0.2', '0.0.3'], 'numpy(>=1.20)': ['0.0.2'], 'numpy(>=1.21)': ['0.0.3']}