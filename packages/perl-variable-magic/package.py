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
#     spack install perl-variable-magic
#
# You can edit this file again by typing:
#
#     spack edit perl-variable-magic
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class PerlVariableMagic(PerlPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url = "https://cpan.metacpan.org/authors/id/V/VP/VPIT/Variable-Magic-0.64.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers("github_user1", "github_user2")

    # FIXME: Add the SPDX identifier of the project's license below.
    # See https://spdx.org/licenses/ for a list.
    license("UNKNOWN")

    version("0.64", sha256="9f7853249c9ea3b4df92fb6b790c03a60680fc029f44c8bf9894dccf019516bd")
    version("0.63", sha256="ba4083b2c31ff2694f2371333d554c826aaf24b4d98d03e48b5b4a43a2a0e679")
    version("0.62", sha256="3f9a18517e33f006a9c2fc4f43f01b54abfe6ff2eae7322424f31069296b615c")
    version("0.61", sha256="b8afe92e54c72a2ed2ca1b08ce90518b855734f7d33c454d0f66f2c1ccf8a6d7")
    version("0.60", sha256="22a5e2bd38ac327f1ae4b4ce654e726f3bba9c1d813750b98165831ea00952cf")
    version("0.59", sha256="e01eb9fd803d8c9baf93f3dbb5cabf750e4bb74eccc8a1f9035e46246a688066")
    version("0.58", sha256="036d6a18b2014fbe3a9e2c033157bd62dd82b175dbe63e12d7c874aed61f10fa")
    version("0.57", sha256="4dc0427c08f608473f84e890d50363ee0f8b271283841f977a3e2dc5b7ad5ca2")
    version("0.56", sha256="ece062c9b22ef352fd1e54cb02878b2498bfeb0577176b77737191fe52a8572b")
    version("0.55", sha256="8f47ebf7d5e11a1c06920e28dd9547f6358fbc64aec804ee0208de42fc16f077")
    version("0.54", sha256="bb0d826a560ef55e959de5c09b12aac004ab5d41cebe55d501102684a5e4282a")
    version("0.53", sha256="18fd97b913b383df0c8f1e91cabe82bfc450d7aec8d5f62f9d015884cf7abed7")
    version("0.52", sha256="0abbdb5cf512d000657195741c731ecec8cb223e1fb7607ef1df11306d22db8d")
    version("0.51", sha256="e47634a244abdbc61454ced28dc71367551ac2e5576ef00427360ef337361f85")
    version("0.50", sha256="94b437f32c9096ce5d7d7423ff00bdc0661d1c93040305ff4045124fe47867fc")
    version("0.49", sha256="31d9e52a38bb32403f62fa116c9198ff37a88ec3d217a04ebe8e820ea0127add")
    version("0.48", sha256="7cfdca9d11d45a105a0fd11a4dc80e531a519923b811303cc84b14eef5d49188")
    version("0.47", sha256="7a91d4263f61b8f8e5649887757e0eb6d925563611fc73834bbd0778668f2a01")
    version("0.46", sha256="780cf9b6326fa25d156255dff0efa1bf0d2bfde172e1203785c0426b945d0e7d")
    version("0.45", sha256="8bac6416485808cd7b42d8e5d95720a301a53357cb73f433efcf7103b8276575")
    version("0.44", sha256="c5494c73bf7f038e98a779843e872f7b6e5a9315b9c1fac139ac03a55950ce1b")
    version("0.43", sha256="dc3def570abd5abf4610d88a4aa88305fce325ee3ef9871c5b6ef736df5b9da8")
    version("0.42", sha256="3f63455c312be0ed2205a475f07e187e88251c76be746250bbdf3092ef750085")
    version("0.41", sha256="2fb0e6befc3191467a12128fe3fada4b6ebbf7b124cdec07d08c7d1d254c2147")
    version("0.40", sha256="21aaa481380f7fee141d4bdf4fbc72d3166792359ebe6abb09a24196e79788f0")
    version("0.39", sha256="995698de43b794e212da5baaeb936123dc6d789060025cdb388fbee362af0aba")
    version("0.38", sha256="34d6556b87a41f9bf7ab81353a3b7b4f7136dbcc1752ab74c1736f9bebc7a445")
    version("0.37", sha256="5831c5e25965c22aca3c0cc7f75bc5fd3b1daadf7209cef9dadad0067d3492c5")
    version("0.36", sha256="15305b54e948f74a0cf77c1c6bd8aa399caac12d6b1dee8cc4a69ff7d1421db6")
    version("0.35", sha256="ac2d3087f39de9fe0cb9209ffe187c4a9b725b8543dd4e3179fe23b8462ace5c")
    version("0.34", sha256="52d8f7de647a606e4e652a9ad68e4db6ade24674c7c756f8727f9d776b465783")
    version("0.33", sha256="24513b11ce72ea9cdb7971311ab38970a1a21681ba79794879b248cd88e1afeb")
    version("0.32", sha256="6e95b17e36fb623809dd56d18f7c0baac1ac3aff6e7927fea5ab7043c933cfcd")
    version("0.31", sha256="755a6f3a13c8b8422ffa5fdce7e3ea3554f6602409da1d3d8213ef4627d33848")
    version("0.30", sha256="80fc6b923bbbef96eb498255690b08b6ccf4568edc73f46f8202ab3d3201f8cc")
    version("0.29", sha256="42efdf6b0ff8594b44392af3a55a3ffd79f051f62650dc87ee85c3ee963f4120")
    version("0.28", sha256="ccb7fc30e15313226c31121546a6edb27a8081784363e60503dd0d1bb4dfe66c")
    version("0.27", sha256="ec6a5b0452be93f2d2aa4f45664f15c72f40e6fc2a5339dd5539563336b8040d")
    version("0.26", sha256="1b1821d0eb3b9254df647ebfa52e7befdef2ec3ef2efd85c666bdf4b8fe740c7")
    version("0.25", sha256="9285a4ce8ac3881c951c608a5478fa49eca5ac31d6bc7a00bf4b1dc35deb04ad")
    version("0.24", sha256="0e9268c5abde8744295ad6a3648a3220defc0272a9348ffbfa004ed99ddaf5df")
    version("0.23", sha256="9906f2d8c42409c52e7ec98cd61b7f33f310d6a691880ecc54e78d16de02a9b8")
    version("0.22", sha256="11352544a63fb875e7e00814e8a9d7cdd20b4c5c35225ba06119e257237888a3")
    version("0.21_02", sha256="c00df6f12ad32cd3abe51d2a99020ab226a8e83abf4a4f6b5ed549e640f67e32")
    version("0.21_01", sha256="e37b78cf6b31abab5cea30039a9f96fbe88f2bc7bd529016fb968d4fa97dd688")
    version("0.20", sha256="e742d326f564757406476c29b54d976871d000b7cf816381f111271f7cac4d57")
    version("0.19", sha256="d5c84f38e38a48a40cea48f4932df28957c8f9b49c6ccb1a94ce7ace914ee64a")
    version("0.18", sha256="c1729f2e6300e0326953503f33234856d9e6ba7ad2d013deb7656f8798b6c3a1")
    version("0.17", sha256="758f7aee2ca18a201d93426b1abfe42e1d63df4f7cbd8e596c40639255a48501")
    version("0.16", sha256="a09b9640d865c5e3cc16abd6d37e4e027cf9cc816f6217d337b49aa4c8281dcd")
    version("0.15", sha256="efe5c11a5cf19dfa9763635d86555dd504344c630b5803671f930e5972da68d5")
    version("0.14", sha256="3686b16760c34f0628bc50cc4494ed59d5acecbfa90c56d0bda8c77fe9ade0d2")
    version("0.13", sha256="d49234a382c2c49e301b53d4e7e89c9189c72058f303dcd60211053a1653a2d7")
    version("0.12", sha256="bbad76a654df9bd1115531800957f4130bfd309ebcdfb27c45d4ea0db560d7d7")
    version("0.11", sha256="7a2873733262235e376765a3a37260dd57431065c9e0139b1243a0a0f105c78c")
    version("0.10", sha256="a44a4e4e70c9d63954a8bb73784f3fbfba914195b7bb13cd3e724deafd266117")
    version("0.09", sha256="2aa74f325e79f51cfa003cbb284547df70ac83164d2ae2b383bbb1cbc22a586d")
    version("0.08", sha256="8d493d147c34d513ce2dfa70113bbc68e867d65e295a1104ff5a414d47523293")
    version("0.06", sha256="8ad5ac5e740908ee5e3123377f77d85a9ed96d2a5b2c98a24d62b53e23a71a0b")
    version("0.05", sha256="ab7b62e083b32387ef20f34e17f00819ebbb533b045c91939916b48e95b87628")
    version("0.04", sha256="e7b8bf0facd285125b5df329439f1123845c6973f27fa754294d443cb843b321")
    version("0.03", sha256="ed92eded58a91937e57f7e6c16117da07d176aeb82429b7a4d84366d53b28028")
    version("0.02", sha256="e0a12ea95de0f3a4cce6a03bceafce22e341230c625723d1c71346b53f2f1256")
    version("0.01", sha256="dba1ca85cf04af2e2d5413d45684a715e1a9866d40a7c193dd6d49a3cc978919")

    # FIXME: Add dependencies if required:
    # depends_on("perl-foo", type=("build", "run"))

    def configure_args(self):
        # FIXME: Add non-standard arguments
        # FIXME: If not needed delete this function
        args = []
        return args
