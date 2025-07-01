# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyCellsnp(PythonPackage):
	"""cellSNP - Analysis of expressed alleles in single cells"""
	
	homepage = "https://github.com/huangyh09/cellSNP"
	pypi = "cellSNP/cellSNP-0.3.2.tar.gz" 

	version("0.0.6", sha256="66e01ede8b68f69bcc6293e05e8345c1e315feda55c3f03399fbf78e9febfff9")
	version("0.0.7", sha256="ad172a748a8a6d7f1283ceffc4760d1edc34ea77d3e2f3185cca88451eaf4e6b")
	version("0.0.8", sha256="c83277a0f17f5ba8d4855b975f8e5051638d81fa011ad16422dc890aee0b8bc5")
	version("0.1.0", sha256="ef23e8b6d71854c65a2a74846a7c9e1ce671440cfd2cea377d131a94e5f39a7b")
	version("0.1.1", sha256="49ec2969ae4d448171803227776ffb6698fa856370ec05c7dc30c4b8501cfb51")
	version("0.1.2", sha256="864d442798861fdded91b9ff1b3376ed2ae0fdfc6607dd8750ea7d92471f1dfe")
	version("0.1.3", sha256="bdc30f747c88d20f3ab77f0bb39d84c67dc1650904c93a13ad72a80d10f1c735")
	version("0.1.4", sha256="91e4904ef3fd1773ba3c790dc8e6b2987215ccf87d7b130ac21a8ab397c81f6a")
	version("0.1.5", sha256="550e1009cc2af2dc80dd0ad03981d0f286f74f5c86d470f665ea71ec4ed84d3b")
	version("0.1.6", sha256="9efe9d4dc1874e9d3b3c5decbb982b94805ea6da4959b5fec464e45d8e5ef680")
	version("0.1.7", sha256="dad0e157da312b347cad55ebbe4a79a4c2a0b9af7dcf7c38be79ca4726f84709")
	version("0.3.0", sha256="1c4945b82f6e9deb9ccdff57ce52878ab52e9e634ee1051c76472c49d555dd16")
	version("0.3.1", sha256="7a1bd4918da4ebfaa21c01f9745a6e5664a2149868b1999c807f75c2ec1c5132")
	version("0.3.2", sha256="4b5f72f9c553a39ad7726b20545b9f053f79e9c3a1dfa6bd19fdcd78aa5ec2dd")

	depends_on("py-setuptools", type=("build"))
