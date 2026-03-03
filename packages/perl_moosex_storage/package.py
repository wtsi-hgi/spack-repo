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
#     spack install perl-moosex-storage
#
# You can edit this file again by typing:
#
#     spack edit perl-moosex-storage
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class PerlMoosexStorage(PerlPackage):
    """A serialization framework for Moose classes."""

    homepage = "https://metacpan.org/pod/MooseX::Storage"
    url = "https://cpan.metacpan.org/authors/id/E/ET/ETHER/MooseX-Storage-0.53.tar.gz"

    version("0.53", sha256="8704bfe505f66b340f62e85c9ff319c19e9670b26d4b012c91f4e103b1daace0")
    version("0.52", sha256="510ebe46e4b19d1bbf92492e0f659787eec53e8e0cc281cb49d4e8567fcd68ea")
    version("0.51-TRIAL", sha256="3b45c203611176184c6bc5b794d375cc57f74b96ef96140c763f602f9abb5aa1")
    version("0.50", sha256="432aed0023a0431006f83e7baf0daaea27e62ab3403f2804965892e8a9111f9a")
    version("0.49", sha256="f4339b3631f7272fb582924c94c74a2653b75a689bcd95121bbbf853f342f629")
    version("0.48", sha256="a8551f6276cddb93255b1dbecab3444883f95571cefb57a515189fe11ac1f7ed")
    version("0.47", sha256="1d9fd66cd7b5e3b7a3978ceb2358a11a29961ea4d1c082750b0abda2a72d1a25")
    version("0.46", sha256="95d6b8487527252772d13b4bff20a1cee7c7fbbb5a156a4a8f3d64c04d0009d6")
    version("0.45", sha256="ea35f0a9a6ae3228b24b4c39f968cac7270205520b9369392af08ac7251bc13a")
    version("0.44", sha256="8fa57f8eeb5010bfc29b9c3d61fb543f9a344dc8c0ea071d95416fd43c08f23f")
    version("0.43", sha256="bd4cc1bfc259f94f38e70c738d8a1656c939c7d8ccd872748b64ad24ae19bae6")
    version("0.42", sha256="eebb5e12e48d70632f7d15a46373bf612ea44beba329b18d7a51c9f3a9c44d6d")
    version("0.41", sha256="ab7839c4568b2cc3013d54d11f22407b915a53e74b83ff6288afb5e851a7ed0a")
    version("0.40", sha256="11a166eedec3db3507c58ab7192f06d81ca6f2c2ba47e1fa193a704b9b321d3b")
    version("0.39", sha256="66779abce711a8d9e3f49a17ccc10687bc1c0863b7b049e3bbb26736b6b3d802")
    version("0.38-TRIAL", sha256="332a7d630168e05fbe8931f5b7838fbbc32018296bb6d64ab79a3c5667d41803")
    version("0.37-TRIAL", sha256="b8bb6c855936d2978353dea02dcc7e89457ab6b66c9bd4dfb87163faa9dc1dcc")
    version("0.36-TRIAL", sha256="5e90b9b4beada1c9cc788f730e121bf1316f0905655cee84474d966c7b24994d")
    version("0.35", sha256="ad4b2c2e385d70154e8c5620eff6a67054a474b58dc4062ff362ef1c0842e63d")
    version("0.34", sha256="40e9bb7ff6bc1e0d1b45b87d6e1290cc8fab0c96c93d8793c4c99376a0584436")
    version("0.33", sha256="96eae36cb97105047ee8f36e3a8b0e4ef388dde460d5cb84fa4b1e1f248853d0")

    depends_on("perl-json-maybexs", type=("build", "run"))
    depends_on("perl-test-deep-json", type=("build", "run", "test"))
    depends_on("perl-yaml", type=("build", "run"))
    depends_on("perl-test-without-module", type=("build", "run", "test"))
    depends_on("perl-io-stringy", type=("build", "run"))
