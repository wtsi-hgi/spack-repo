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

    version("1.10.1", commit="953a03226e4a40e90145ba3d05ea5d18cdd7cae0")
    version("1.4.0", commit="e92dde559097e80af674ffebfde12a80c826a5c8")

    depends_on("r@4.2:", type=("build", "run"))
    depends_on("r-protgenerics@1.9.1:", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-spectra", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-qfeatures", type=("build", "run"))
    # Missing runtime dependency reported by install logs
    depends_on("r-dbi", type=("build", "run"))
