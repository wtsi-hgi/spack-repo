# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSignac(RPackage):
	"""Analysis of Single-Cell Chromatin Data.

	A framework for the analysis and exploration of single-cell chromatin data.
	The 'Signac' package contains functions for quantifying single-cell
	chromatin data, computing per-cell quality control metrics, dimension
	reduction and normalization, visualization, and DNA sequence motif
	analysis. Reference: Stuart et al. (2021)
	<doi:10.1038/s41592-021-01282-5>."""

	license("MIT")

	cran = "Signac"
	version("1.16.0", sha256="71750f98af3b9e40ddcf52a7b665d33e3cefd0d63837f07cc3c54af807e109bf")
	version("1.15.0", sha256="672d8ba06f4ff06fd00009bf70db5a11817246b24fd002cbd55944fe1bd8ed9a")
	version("1.14.0", sha256="e0aad9e2c27c148fdd376081c2de1e3db46b1835eac83ef41fe562e08363c59e")
	version("1.13.0", sha256="d9b4103c6437391834b2d9e2aab8829f186b6e09d070dfe2a66cc12583241b2a")
	version("1.12.0", sha256="0a4f1e53bcb6c3ba1e3a8e0800d6c4e65983560ff1147a643b7109452374c937")
	version("1.11.0", sha256="0daac539a4ca6d7f4c779fc06e77ffed4faca3e0689d3fb47d960edb4032f1c5")
	version("1.10.0", sha256="75c274dfc49b0f1478adfdd85e9acbf04d3fae38f2ebe31658a1ba17a7880994")
	version("1.9.0", sha256="b8ff36427e5919fd420daa1f50cf8c71935293ee7f88560041acb993b5e3afa8")
	version("1.8.0", sha256="9c4b123f4d077111c7e6dd1659483ada984300c8e923672ca924e46fb6a1dd06")
	version("1.7.0", sha256="5e4456eeab29fa2df7f6236b050dec8cb9c073d7652a89ee5030a27f94e5e4bf")

	with default_args(type=("build", "run")):
		with when("@:1.13.0"):
			depends_on("r@4:")
		with when("@1.14.0:1.16.0"):
			depends_on("r@4.1:")

		depends_on("r-genomeinfodb@1.29.3:")
		depends_on("r-genomicranges")
		depends_on("r-iranges")
		depends_on("r-matrix")
		depends_on("r-rsamtools")
		depends_on("r-s4vectors")

		with when("@:1.13.0"):
			depends_on("r-seuratobject@4:")
		with when("@1.14.0:1.16.0"):
			depends_on("r-seuratobject@5.0.2:")

		depends_on("r-data-table")
		depends_on("r-dplyr@1:")
		depends_on("r-future")
		depends_on("r-future-apply")
		depends_on("r-ggplot2")
		depends_on("r-rlang")
		depends_on("r-irlba")
		depends_on("r-pbapply")
		depends_on("r-tidyr")
		depends_on("r-patchwork")
		depends_on("r-biocgenerics")
		depends_on("r-stringi")
		depends_on("r-fastmatch")
		depends_on("r-rcpproll")
		depends_on("r-scales")
		depends_on("r-rcpp")
		depends_on("r-tidyselect")
		depends_on("r-vctrs")
		depends_on("r-lifecycle")
	
	depends_on("zlib", type=("build", "link", "run"))
