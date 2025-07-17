# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RModcon(RPackage):
    """Modifying splice site usage by changing the mRNP code, while maintaining the genetic code

    Collection of functions to calculate a nucleotide sequence surrounding for splice donors sites to either activate or repress donor usage. The proposed alternative nucleotide sequence encodes the same amino acid and could be applied e.g. in reporter systems to silence or activate cryptic splice donor sites.
    """

    homepage = "https://github.com/caggtaagtat/ModCon"
    bioc = "ModCon"

    version("1.16.0", commit="2ead6d76c213099399d26eebd48153d747ae3e64")
    version("1.10.0", commit="05c979f6af16458ca6ed9dbc67bcd0933e6b9ccf")

    depends_on("r-data-table", type=("build", "run"))
    depends_on("r@4.1:", type=("build", "run"))
    depends_on("perl", type=("build", "link", "run"))
