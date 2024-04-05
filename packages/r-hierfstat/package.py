# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHierfstat(RPackage):
	"""Estimation and Tests of Hierarchical F-Statistics

	Estimates hierarchical F-statistics from haploid or
    diploid genetic data with any numbers of levels in the hierarchy, following the
    algorithm of Yang (Evolution(1998), 52:950).
    Tests via randomisations the significance
    of each F and variance components, using the likelihood-ratio statistics G
    (Goudet et al. (1996) <https://academic.oup.com/genetics/article/144/4/1933/6017091>).
    Estimates genetic diversity statistics
    for haploid and diploid genetic datasets in various formats, including inbreeding and
    coancestry coefficients, and population specific F-statistics following
    Weir and Goudet (2017) <https://academic.oup.com/genetics/article/206/4/2085/6072590>.
	"""
	
	homepage = "https://www.r-project.org"
	cran = "hierfstat" 

	version("0.5-7", sha256="a38eb5758e3fc3683ec83f94138525eed3d8b7e330f894bab2f821557e98e836")
	version("0.5-11", sha256="816c03c98135d78ad26e74656a7d0ec00c5052f75aafe6775215651a1228cb5b")
	version("0.5-11", md5="9bc78ee3f9bbe0fe2ab9e44c5bff40cf")
	version("0.5-10", sha256="991ce4766c98ee741e0cc4f7da8e2e4a25c93a8eda2fd9cb1a4a171494a59bdc")
	version("0.04-6", sha256="b0deb9988e6acb491918709b986e59cf6d6d3804a3ca231854d6b5acd0dcba54")
	version("0.04-4", sha256="31b8ceca176285f61a2103de990d8c33d0bba832b430a30a8fb6da1454d68cfe")
	version("0.04-3", sha256="2f0329525ed2c7973249d7b88c59235cb4377f28288a817e18fbfb162b065f4a")
	version("0.04-22", sha256="ddf9151b7492c8d13619402bf3bad741a4ea3a2fdb28e7c29a659b94c4165bb9")
	version("0.04-2", sha256="c161837e8fa8cca077e091843fc98ffa8bf50b442a3cd34fc9e5cfe73ed50faf")
	version("0.04-14", sha256="4c8434fcb0b2f1ae93a9e8c2b32c1d6970f715c0e285f8e803bb4506302b747d")
	version("0.04-10", sha256="f4bd092646d8a696c87c01259752b180e4a5b1bbbded410eebc36d1e69b116d8")
	version("0.04-1", sha256="20147d32ada53c7198f86869482747406ac4cfce23336b7c34e841dd13671bfb")
	version("0.03-3", sha256="92d10a79b6c01467844cc2dade9cc7158e8912e5f57ad50d7fdf3eaa0b73cc8b")
	version("0.03-1", sha256="f2e406e550c69b602dc60b95b8ef3021a42ae6587f442d476e8985450edae8d8")
	version("0.02-2", sha256="c6a21492738d0293de951a501f19a443459e1c4cedfbecbbcb5938a7b473d621")
	version("0.01-4", sha256="71d1ac2c9c86b52c0db2cf72b4a912bcd61be24c2daaf4766dbda5006fe0a2f1")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ade4", type=("build", "run"))
	depends_on("r-adegenet", type=("build", "run"))
	depends_on("r-gaston", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
