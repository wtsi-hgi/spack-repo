# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install perl-moosex-types
#
# You can edit this file again by typing:
#
#     spack edit perl-moosex-types
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class PerlMoosexTypes(PerlPackage):
    """Organise your Moose types in libraries."""

    homepage = "https://metacpan.org/pod/MooseX::Types"
    url = "https://cpan.metacpan.org/authors/id/E/ET/ETHER/MooseX-Types-0.50.tar.gz"

    version("0.50", sha256="9cd87b3492cbf0be9d2df9317b2adf9fc30663770e69906654bea3f41b17cb08")
    version("0.49", sha256="aa54504655518853f5b4f353a9b317039fc902ab7bd14a0871eea52479036984")
    version("0.48", sha256="b8ecaf4a2099780909a4269b9e53a08511073ec7c73ae61c83b7a1e3007aa875")
    version("0.47", sha256="505280c447393a04b5937c2f1e3c040cf35fa8b05f02053804892fa2593f02ba")
    version("0.46", sha256="e9e8c36284cf1adc6563c980c0a4f0a7df720dbaaece0dd6be66b975dde5db7a")
    version("0.45", sha256="d01ff4a3db78e1150101b4b63569e4bce3ced3b5b0024c52c87575e0820609c7")
    version("0.44", sha256="677aca6de01d07a8bda480784e972a6ea93a7f1d0513c7522aa7d9838d4310cc")
    version("0.43-TRIAL", sha256="23a522b9448f2cff59eb076917119c0aeb7f890e9904ff3846c4c6068140e9f8")
    version("0.42-TRIAL", sha256="6ea0dabaf90acd01bb4008ba9e1c281bff021300ee8b627fe48d9d7573d75252")
    version("0.41", sha256="846d12cb0fc4048e06fae5e5fdf053e78f2a9fd444ddfc355245d4ae0482fea4")
    version("0.40", sha256="8851e85c153e6f77c417f66e557dd86fc2f5ad7ee148bcafa4d159eebd83e2ff")
    version("0.39", sha256="c3db60b897acecf620f3bf7e62125d1201e34861ba70ecf1f084b1ae363b46af")
    version("0.38", sha256="3f575a744de79629166a5cf50acb0a1f3608ece6e0d9cd5153ee87336928fc2a")
    version("0.37", sha256="2fa88670023ee77c6e5fc83c68bb6c1061ee89e1857ea59f767ab04f3bb4d37a")
    version("0.36", sha256="cf73a14fa67ca3070b76e071a933fae87b8daf1dbc48970d8461884ee9f8e9aa")

    depends_on("perl-module-build", type="build")
    depends_on("perl-moose", type=("build", "run"))
    depends_on("perl-namespace-autoclean", type=("build", "run"))
    depends_on("perl-carp-clan", type=("build", "run"))
    depends_on("perl-sub-exporter-formethods", type=("build", "run"))
