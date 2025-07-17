# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlowworkspacedata(RPackage):
    """A data package containing two flowJo, one diva xml workspace and the associated fcs files as well as three GatingSets for testing the flowWorkspace, openCyto and CytoML packages.

    The necessary external data to run the flowWorkspace and openCyto vignette is found in this package.
    """

    bioc = "flowWorkspaceData"

    version("3.20.0", commit="c3d7b139f50068d0037c95c86bb9e06cc9b99c40")
    version("3.14.0", commit="4561f3dbdd0223657db10cdafe5a8b35a40a9aff")
