# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpectra(RPackage):
	"""Spectra Infrastructure for Mass Spectrometry Data

	The Spectra package defines an efficient infrastructure for storing and handling mass spectrometry spectra and functionality to subset, process, visualize and compare spectra data. It provides different implementations (backends) to store mass spectrometry data. These comprise backends tuned for fast data access and processing and backends for very large data sets ensuring a small memory footprint.
	"""
	
	homepage = "https://github.com/RforMassSpectrometry/Spectra"
	bioc = "Spectra" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Spectra_1.12.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/Spectra/Spectra_1.12.0.tar.gz"]

    version("1.18.2", tag="RELEASE_3_21")
	version("1.12.0", sha256="1e0f13135f9f24e06f485a839355c0b5453fc6d649f4c2248bfcf7ef4a4ffa1f")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-protgenerics@1.33.1:", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-mscoreutils@1.7.5:", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-metabocoreutils", type=("build", "run"))
