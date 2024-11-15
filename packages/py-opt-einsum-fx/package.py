# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyOptEinsumFx(PythonPackage):
	"""Einsum optimization using opt_einsum and PyTorch FX"""
	
	homepage = "https://github.com/Linux-cpp-lisp/opt_einsum_fx"
	pypi = "opt-einsum-fx/opt_einsum_fx-0.1.4-py3-none-any.whl" 

	version("0.1.1", sha256="30b52b3f7997f62b87f770340719bb14d416d50572739b70f75baea93f9fa1cd")
	version("0.1.2", sha256="dcf4f8ca1bf16734d6a14bba5d669936f064c122839a76a44b279170825ecd6e")
	version("0.1.3", sha256="358b88ea40c462f8376b38f4f40b577dded515ad93ea9c67fadcb03726153979", expand=False, url="https://files.pythonhosted.org/packages/b0/cc/a361139b500573dd78aef322bba6053c6c7c9e1cccb466ae8ea10629725d/opt_einsum_fx-0.1.3-py3-none-any.whl")
	version("0.1.4", sha256="85f489f4c7c31fd88d5faf9669c09e61ec37a30098809fdcfe2a08a9e42f23c9", expand=False, url="https://files.pythonhosted.org/packages/8d/4c/e0370709aaf9d7ceb68f975cac559751e75954429a77e83202e680606560/opt_einsum_fx-0.1.4-py3-none-any.whl")

	depends_on("py-setuptools", type=("build"))
	depends_on("python@3.6:", type=("build", "run"))
	depends_on("py-torch", type=("build", "run"))
	depends_on("py-opt-einsum", type=("build", "run"))
	depends_on("py-packaging", type=("build", "run"))

# {'torch(>=1.8.0)': ['0.1.3', '0.1.4'], 'opt-einsum': ['0.1.3', '0.1.4'], 'packaging': ['0.1.3', '0.1.4']}