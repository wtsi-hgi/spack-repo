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
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/LungCancerLines_0.40.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/LungCancerLines/LungCancerLines_0.40.0.tar.gz"]

    version("0.46.0", tag="RELEASE_3_21")
	version("0.40.0", sha256="86688a5c0915c1522fb1792accd37c36c3a8c5524dc3a4cda77c5a62d2a1277b")

	depends_on("r-rsamtools", type=("build", "run"))

