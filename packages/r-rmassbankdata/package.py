# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRmassbankdata(RPackage):
    """Test dataset for RMassBank

    Example spectra, example compound list(s) and an example annotation list for a narcotics dataset; required to test RMassBank. The package is described in the man page for RMassBankData. Includes new XCMS test data.
    """

    bioc = "RMassBankData"

    version("1.46.0", commit="32357856b5adfd3ba32913ff4439dd2015329f80")
    version("1.40.0", commit="07e0702bd51e94c8d4cf45b3f90337aadebbb65e")
