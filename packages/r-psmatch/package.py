# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPsmatch(RPackage):
    """Handling and Managing Peptide Spectrum Matches

    The PSMatch package helps proteomics practitioners to load, handle and manage Peptide Spectrum Matches. It provides functions to model peptide-protein relations as adjacency matrices and connected components, visualise these as graphs and make informed decision about shared peptide filtering. The package also provides functions to calculate and visualise MS2 fragment ions.
    """

    homepage = "https://github.com/RforMassSpectrometry/PSM"
    bioc = "PSMatch"

    version("1.12.0", commit="18c18133b9d3223898cb645a86efdc67562c24af")
    version("1.6.0", commit="f3d59df4c1b2b26c0d92792d4fffa22650b86ebc")

    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-igraph", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-protgenerics@1.27.1:", type=("build", "run"))
    depends_on("r-qfeatures", type=("build", "run"))
    depends_on("r-mscoreutils", type=("build", "run"))
    # Missing in recipe but required by DESCRIPTION
    depends_on("r-spectra", type=("build", "run"))
