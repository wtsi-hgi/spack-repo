# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAgilp(RPackage):
	"""Agilent expression array processing package.

	More about what it does (maybe more than one line)."""

	bioc = "agilp"
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/agilp_3.34.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/agilp/agilp_3.34.0.tar.gz"]

    version("3.40.0", tag="RELEASE_3_21")
	version("3.8.0", commit="c772a802af1b4c0741f2edd78053a0425160ea53")
	version("3.34.0", sha256="8a201ed954249d8f8125901f208c6cb7f10c31fc6637cb831afe48bb6c656b75")
	version("3.32.0", commit="8291f7b7c1b6167952568f51593116afc6d0fc27")
	version("3.30.0", commit="a2c898dc901ccdda4b8582caff079ab20b1bfc28")
	version("3.28.0", commit="2c6dfccc76473b5bef13b75fa59adf46b3381f55")
	version("3.26.0", commit="3170fe2b1cc459d5e2ca7f61a127aac17cd66a96")
	version("3.22.0", commit="7d089d576752e0526f15a1007e94436089954313")
	version("3.16.0", commit="2900d6066317f21d076b3a043b16f32eca168c47")
	version("3.14.0", commit="8feb047d70216013462ea7806e9227d192b60c61")
	version("3.12.0", commit="a86dea1b03b2b56c2c8317d4b10903fb8948ffcb")
	version("3.10.0", commit="cffec1004704a0c5119a50e3ad474897978981be")

	depends_on("r@2.14:", type=("build", "run"))
