# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyScikitMdr(PythonPackage):
	"""Multifactor Dimensionality Reduction (MDR)"""
	
	homepage = "https://github.com/EpistasisLab/scikit-mdr"
	pypi = "scikit-mdr/scikit_MDR-0.4.5-py3-none-any.whl" 

	version("0.1", sha256="b19ee888b6b90ac172032cffaf46ea28ef6bd4bf7a54602d6d594b31ecdb5b09")
	version("0.2", sha256="1ea5c0ff1b323c39641c151c67874f7534808674aab2f82659e4f3d40e6ade9a")
	version("0.3.0", sha256="f54bb97fbbf290d54296d28c06d765ad563334a0fa2f14e7be1bcfcb45850ce5")
	version("0.3.1", sha256="3216d4c581bc70c5f794cff220a52a39b07d8f5031464a26a55fa13a8d303ef2")
	version("0.3.2", sha256="f92c311ff0e81c5b3466cfcd572ce0cccefaabffbd1ed494c21bb7564f0c04da")
	version("0.4", sha256="aaa027ceb29d96973ef1940b115dc6a7c040804c22948eae7e15468dd3dd0b6f")
	version("0.4.1", sha256="afaf54b59e139a260719e40c3913d63d85ecf0bfda3c27bd96013545e9395fbb")
	version("0.4.2", sha256="9c67e1423f5b7a90bdef9aef1cd6a46b79f2527ab1686b8b72e45be64188f0e6")
	version("0.4.3", sha256="e5a28fb8160bd2665705c97534d94a1a1889f199c04b09878f27f6513a6f712e")
	version("0.4.4", sha256="fc4e6710c7ac7a63c55641773388e43cc75bbe19f8d946bb8ac09eadb7d9eb2e")
	version("0.4.5", sha256="9261a0a68fff658edbd14719bdfac5e5518f30a58dd11f380b7d88a50af8b854", expand=False, url="https://files.pythonhosted.org/packages/44/53/e770cc5d19b8025632a779529c6e2b6d37eeaec7200e27d4a62a426d68d0/scikit_MDR-0.4.5-py3-none-any.whl")

	depends_on("py-setuptools", type=("build"))
	depends_on("py-matplotlib", type=("build", "run"))
	depends_on("py-scikit-learn", type=("build", "run"))
	depends_on("py-scipy", type=("build", "run"))
	depends_on("py-numpy", type=("build", "run"))

# {'numpy': ['0.4.5'], 'scipy': ['0.4.5'], 'scikit-learn': ['0.4.5'], 'matplotlib': ['0.4.5']}