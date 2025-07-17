# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMeebodata(RPackage):
    """MEEBO set and MEEBO controls.

    R objects describing the MEEBO set.
    """

    homepage = "http://alizadehlab.stanford.edu/"
    bioc = "MEEBOdata"

    version("1.46.0", commit="02b916dd7639020afa14f942b9318e87a2359cdf")
    version("1.40.0", commit="c102a18406ea90088a44d66084961875e8b436f7")
