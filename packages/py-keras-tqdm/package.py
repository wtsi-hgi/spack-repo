# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyKerasTqdm(PythonPackage):
	"""Keras models with TQDM progress bars in Jupyter notebooks"""
	
	homepage = "https://github.com/bstriner/keras-tqdm"
	pypi = "keras-tqdm/keras_tqdm-2.0.1-py2.py3-none-any.whl" 

	version("1.0.1", sha256="37522c77829ec88d9fdf0d7da046168cdb572db6daffe43e441df90f65019aaa", expand=False, url="https://files.pythonhosted.org/packages/1d/0a/416e460009828d91e09f883c66f5a69dd2b5de6196bcc8b70727391ad38a/keras_tqdm-1.0.1-py2.py3-none-any.whl")
	version("1.0.7", sha256="65c1b6e23c37d1c6aa1a4e0c2036e63469b80d9a4b4367bf19e85c9f93cf530c", expand=False, url="https://files.pythonhosted.org/packages/c2/b8/511d641a2a809b17e5ed90e3aa3c58b18f5c600a057327e2a55fc0859357/keras_tqdm-1.0.7-py2.py3-none-any.whl")
	version("2.0.0", sha256="48841c97e6e6efd0a92676db9c43a8f669f74cd56cdd249b2125cb2726287a6a", expand=False, url="https://files.pythonhosted.org/packages/38/cb/a47a8837236071b3002453b8e88bdea3ce70c2ed542b61686f61f2ea5f0e/keras_tqdm-2.0.0-py2.py3-none-any.whl")
	version("2.0.1", sha256="3f5b093d49852fc4c9bfeffdc17c8f3eb98b1e530dbd8cc407cf37d197a1dc3b", expand=False, url="https://files.pythonhosted.org/packages/16/5c/ac63c65b79a895b8994474de2ad4d5b66ac0796b8903d60cfea3f8308d5c/keras_tqdm-2.0.1-py2.py3-none-any.whl")

	depends_on("py-setuptools", type=("build"))
	depends_on("py-tqdm", type=("build", "run"))
	depends_on("py-keras", type=("build", "run"))

# {'keras\r': ['1.0.1'], 'tqdm\r': ['1.0.1', '1.0.7', '2.0.0', '2.0.1'], 'Keras\r': ['1.0.7', '2.0.0', '2.0.1']}