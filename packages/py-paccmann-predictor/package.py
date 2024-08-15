# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPaccmannPredictor(PythonPackage):
	"""PyTorch implementation of PaccMann"""
	
	homepage = "https://github.com/PaccMann/paccmann_predictor"
	pypi = "paccmann-predictor/paccmann_predictor-1.0.0-py3-none-any.whl" 

	version("1.0.0", sha256="64822e1861dcf70e75749348a5ca83b069c02538c33fb0765a982b5d0caa9f30", expand=False, url="https://files.pythonhosted.org/packages/9f/10/8d911dfd0cbbcfa8651b154a925f06dafb7448848ea0705566723421625f/paccmann_predictor-1.0.0-py3-none-any.whl")

	depends_on("py-pytoda", type=("build", "run"))
	depends_on("rdkit", type=("build", "run"))
	depends_on("py-tqdm", type=("build", "run"))
	depends_on("py-pandas", type=("build", "run"))
	depends_on("py-torch", type=("build", "run"))
	depends_on("py-scipy", type=("build", "run"))
	depends_on("py-numpy", type=("build", "run"))

# {'numpy': ['1.0.0'], 'scipy': ['1.0.0'], 'torch>=1.0.0': ['1.0.0'], 'pandas': ['1.0.0'], 'tqdm': ['1.0.0'], 'rdkit': ['1.0.0'], 'pytoda>=1.1.5': ['1.0.0']}