# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMsdata(RPackage):
    """Various Mass Spectrometry raw data example files

    Ion Trap positive ionization mode data in mzML file format.  Subset from 500-850 m/z and 1190-1310 seconds, incl. MS2 and MS3, intensity threshold 100.000. Extracts from FTICR Apex III, m/z 400-450.  Subset of UPLC - Bruker micrOTOFq data, both mzML and mz5. LC-MSMS and MRM files from proteomics experiments. PSI mzIdentML example files for various search engines.
    """

    bioc = "msdata"

    version("0.48.0", commit="a257cc36ea5f147d4a5a93b1875572d420fe0233")
    version("0.42.0", commit="8134dff556025923847c482a350c5684e4622573")

    depends_on("r@3.5:", type=("build", "run"))
