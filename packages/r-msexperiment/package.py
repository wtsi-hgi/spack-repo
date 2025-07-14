# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMsexperiment(RPackage):
	"""Infrastructure for Mass Spectrometry Experiments

	Infrastructure to store and manage all aspects related to a complete proteomics or metabolomics mass spectrometry (MS) experiment. The MsExperiment package provides light-weight and flexible containers for MS experiments building on the new MS infrastructure provided by the Spectra, QFeatures and related packages. Along with raw data representations, links to original data files and sample annotations, additional metadata or annotations can also be stored within the MsExperiment container. To guarantee maximum flexibility only minimal constraints are put on the type and content of the data within the containers.
	"""
	
	homepage = "https://github.com/RforMassSpectrometry/MsExperiment"
	bioc = "MsExperiment" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/MsExperiment_1.4.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/MsExperiment/MsExperiment_1.4.0.tar.gz"]

	version("1.10.1", tag="RELEASE_3_21")
	version("1.4.0", sha256="cf79cbb2db2cd679285cdd5407a46bbf8f816804f736f375c5b20ff88189a01a")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-protgenerics@1.9.1:", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-spectra", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-qfeatures", type=("build", "run"))
