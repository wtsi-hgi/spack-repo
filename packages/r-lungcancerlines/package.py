# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLungcancerlines(RPackage):
	"""Reads from Two Lung Cancer Cell Lines

	Reads from an RNA-seq experiment between two lung cancer cell lines: H1993 (met) and H2073 (primary). The reads are stored as Fastq files and are meant for use with the TP53Genome object in the gmapR package.
	"""
	
	bioc = "LungCancerLines"

	version("0.46.0", commit="12aa3f2af1b1b28ba53f30103e86fcaf3ab37b30")
	version("0.40.0", commit="58601300279232e0cdff1c65ec38a7a59d0906df")

	depends_on("r-rsamtools", type=("build", "run"))

