# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyCyvcf2(PythonPackage):
    """fast vcf parsing with cython + htslib"""

    homepage = "https://github.com/brentp/cyvcf2"
    pypi = "cyvcf2/cyvcf2-0.11.7.tar.gz"

    license("MIT")

    version(
        "0.31.1",
        sha256="00bd0e09a3719d29fbc02bc8a40a690ac2c475e91744648750907d1816558fc5",
    )
    version(
        "0.31.0",
        sha256="1480091ad055e8715e8fbbd9a93f3c10655d87a1716ffd122657f42355a23ea4",
    )
    version(
        "0.30.28",
        sha256="dde7771570e210df9ca6d21c171a8aa376f191966826241fdcdf960befb9cc0f",
    )
    version(
        "0.30.27",
        sha256="f1b12c1fb78bd039c5d94b0ff2d838edfa0716c0e4902ad3ecec3d48da3d4ff9",
    )
    version(
        "0.30.26",
        sha256="e8473957181ef7b037213d110217046d107cd6a0eb4671f13c47a7a24412db05",
    )
    version(
        "0.30.25",
        sha256="40f1fda66e3bad9873bba08fe3c0839f590089137b2aa7070247561e77ce0d8d",
    )
    version(
        "0.30.22",
        sha256="324613c41f9bbb322533f351fd8d33a4454b391d76841da0a28a7075a0e15d84",
    )
    version(
        "0.30.20",
        sha256="512be337a4f008ee64ac3a673b0b36769d6e5709b7da0bd0e6b3c8386b1f7248",
    )
    version(
        "0.30.18",
        sha256="2a4de3255e8275275edccf9c2b222cf0eefdab924f0c7cc5ef5503d376f5618a",
    )
    version(
        "0.30.17",
        sha256="abb86cf658838bcd82d2b5d9660d6eff1fc23927fb071edf0c3364716bf4c56a",
    )
    version(
        "0.30.16",
        sha256="8d48f0d09d8d400c05ac44cbbe173545eda00f6ee484be2aab966922715d8073",
    )
    version(
        "0.30.15",
        sha256="8ed8b42f8518e107b471bbec02ef21478cae49f48207f348f8457dafd35c43da",
    )
    version(
        "0.30.14",
        sha256="cc297ff608ed15335c233f965e078b9ca7def3dcec7399951ba1f03c5acc98f1",
    )
    version(
        "0.30.12",
        sha256="14c757b4f771672d3407a00cb0f40db940a317237418ad013b448af89f0c0074",
    )
    version(
        "0.30.11",
        sha256="bf544327b9c9be2491db0af887a98008cdae4d63ee72409960b9d21e572303a7",
    )
    version(
        "0.30.9",
        sha256="8f8ffcd6eeef7a86c8297c27aaff240fc6efa1cbf2169153152f8bf5c34df084",
    )
    version(
        "0.30.4",
        sha256="5088c1df2f1569392395c2e4c93e749149cd18e8e914257077581ee2fdb226a8",
    )
    version(
        "0.30.1",
        sha256="c9e9ebfd425ebdda16c2f2004611fb80bf2cb2b7224f2505e6de8d212da073a1",
    )
    version(
        "0.20.9",
        sha256="e05d4e970d9048b1b779054c33970a908bd4c639e8b681e0a93ef443fdb95b28",
    )
    version(
        "0.20.8",
        sha256="4cabce94a50be2ad9baeef17222a9bae0d7a9e6788aff4c21e09d84c44564d74",
    )
    version(
        "0.20.7",
        sha256="13847815cc6700f3131b27e8b082101a804772bcafe7c4252c3c70fdb3e9f4f0",
    )
    version(
        "0.20.6",
        sha256="3b4c2924109750df9df853df8b754e39d201db18bc2974e6e95a87baf64da561",
    )
    version(
        "0.20.5",
        sha256="a831781f20f2fc35173eaa1d13363fe38ea5ac3d6c004144f0b4c71afb091737",
    )
    version(
        "0.20.4",
        sha256="4e44a0aec80b31af91a4a45e879815bc251ec7e980633d492b672df3101d4d0d",
    )
    version(
        "0.20.3",
        sha256="0747a862cdf930830c1add1cbc7da4f356c1a4cad4565aae4e385ede0499c645",
    )
    version(
        "0.20.1",
        sha256="235135edc79f58015755aa493e4357acbde54a4f67fa5ab8cc24c1506404bbd9",
    )
    version(
        "0.20.0",
        sha256="995364e4cbd97f172bd775249eee24ca61978af153f280c788e804a7d0196601",
    )

    depends_on("py-setuptools", type="build")
    depends_on("automake", type="build")
    depends_on("autoconf", type="build")

    depends_on("htslib", type=("build", "run", "link"))
    depends_on("py-cython@0.23.3:", type="build")
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-coloredlogs", type=("build", "run"))
    depends_on("py-click", type=("build", "run"))
    depends_on("curl")

    def setup_build_environment(self, env):
        env.set("CYVCF2_HTSLIB_MODE", "EXTERNAL")
