<div align="center">

<img src="assets/banner.gif" alt="millia's corner">

<img src="assets/marquee.svg" alt="welcome to my corner of the internet" width="640">

<img src="assets/blinkie-work.gif" alt="open to work">
<img src="assets/blinkie-nix.gif" alt="nix or die">
<br>
<img src="assets/blinkie-k8s.gif" alt="kubernetes survivor">
<img src="assets/blinkie-fish.gif" alt="i use fish btw">
<br>
<img src="assets/blinkie-wine.gif" alt="wine is not an emulator">
<img src="assets/blinkie-term.gif" alt="terminal dweller">
<br>
<a href="https://www.youtube.com/watch?v=VBZA_15mGGU" title="ateez music video"><img src="assets/ateez.gif" alt="ateez"></a>
<a href="https://www.youtube.com/watch?v=KhTeiaCezwM" title="mamamoo music video"><img src="assets/mamamoo.gif" alt="mamamoo"></a>

</div>

<img src="assets/rule.gif" width="100%" height="6" alt="">

### `*~*~*` about me `*~*~*`

platform engineer. i build the boring reliable layer under other people's services, and small
sharp tools for myself when the existing ones give up.

most of what i do professionally is private, so this page is the part you can read: macos
internals, terminal tooling, and a wine runtime that should not work but does.

**open to work** &nbsp;·&nbsp; [dappy.lgbt](https://dappy.lgbt)

<img src="assets/rule.gif" width="100%" height="6" alt="">

### `*~*~*` things i built `*~*~*`

<details>
<summary><b>ratatouille</b> &nbsp;·&nbsp; go &nbsp;·&nbsp; a TUI cleaner for mac</summary>

<br>

macos says "system data: 235 gb" and then refuses to elaborate. `rat` answers the question:
where the space went down to the directory, what is safe to remove with the evidence for each
call written down, and whether the drive itself is healthy.

it never removes anything you did not mark, and it logs everything it does.

[→ dappermint/ratatouille](https://github.com/dappermint/ratatouille)

</details>

<details>
<summary><b>glass</b> &nbsp;·&nbsp; go &nbsp;·&nbsp; a live console for running go services</summary>

<br>

erlang ships a remote shell, rails ships a console, go ships a debugger. glass is the missing
one. three lines in `main`, then attach over a unix socket and read or poke live objects while
the service takes traffic.

```go
in := glass.New()
in.Define("stats", stats)
console.Serve("/tmp/app.sock", in)
```

[→ dappermint/glass](https://github.com/dappermint/glass)

</details>

<details>
<summary><b>winecx-gptk</b> &nbsp;·&nbsp; c, ci &nbsp;·&nbsp; a gptk wine runtime that should not work</summary>

<br>

apple's game porting toolkit only executes on crossover-derived wine builds, because d3dmetal
patches their unixcall internals at load time. so i rebased crossover 26.3's wine diff onto
upstream wine 11.15 via a synthetic three-way merge and put the whole thing in ci.

steam's ui end to end, d3d12 through d3dmetal at feature level 12_2, dxvk, msync. the
llvm-mingw bug that stalled steam's login took a module bisection to find.

[→ dappermint/winecx-gptk](https://github.com/dappermint/winecx-gptk)

</details>

<details>
<summary><b>wlipurk-appkit</b> &nbsp;·&nbsp; nix &nbsp;·&nbsp; hermetic flipper app builds</summary>

<br>

a fap only runs if it was built against the exact firmware sdk it loads on, and the official
catalog will not serve our custom flipper fork. this pins fbt's toolchain in a nix flake and
builds catalog apps from source against our own sdk, with no network reach at build time.

[→ dappermint/wlipurk-appkit](https://github.com/dappermint/wlipurk-appkit)

</details>

<details>
<summary><b>samsung-ac-remote</b> &nbsp;·&nbsp; c &nbsp;·&nbsp; because my remote broke</summary>

<br>

samsung a/c has no one-shot ir codes, only full state frames with a dual-section checksum. so
every button press retransmits the entire state: power, mode, temperature, fan, swing.

a flipper zero fap, built against the f6/f7 fbt sdk.

[→ dappermint/samsung-ac-remote-flipper-app](https://github.com/dappermint/samsung-ac-remote-flipper-app)

</details>

<img src="assets/rule.gif" width="100%" height="6" alt="">

### `*~*~*` the day job `*~*~*`

kubernetes clusters and the pipelines that feed them. eks, karpenter, helm, k9s when something
is on fire. infrastructure in opentofu and ansible, secrets in vault and sops, aws underneath.

the parts i actually care about: making deploys uneventful, making the failure mode legible
before someone has to guess, and deleting the runbook step that a machine should have been
doing. none of it is public, which is the nature of the work, so take the repos above as
evidence of how i think instead.

<img src="assets/rule.gif" width="100%" height="6" alt="">

### `*~*~*` stack `*~*~*`

**languages** &nbsp; go · swift · c · nix · python

**platform** &nbsp; kubernetes · eks · karpenter · helm · k9s · opentofu · ansible · vault · sops · aws

**day to day** &nbsp; macos on nix-darwin · fish · a flipper zero that has ruined several
evenings

<div align="center">

<br>

<img src="assets/construction.gif" alt="under construction">

<sub>this page is never finished. that is the point.</sub>

<img src="assets/rule.gif" width="100%" height="6" alt="">

<a href="https://nixos.org"><img src="assets/btn-nix.gif" alt="made with nix"></a>
<a href="https://go.dev"><img src="assets/btn-go.gif" alt="powered by go"></a>
<a href="https://github.com/dappermint/ratatouille"><img src="assets/btn-term.gif" alt="best in a terminal"></a>
<a href="https://github.com/dappermint/Whisky"><img src="assets/btn-swift.gif" alt="swift on macos"></a>
<a href="https://dappy.lgbt"><img src="assets/btn-site.gif" alt="dappy.lgbt"></a>
<a href="https://flipperzero.one"><img src="assets/btn-flip.gif" alt="flipper zero"></a>

<br><br>

<img src="https://komarev.com/ghpvc/?username=dappermint&style=pixel&color=ff00dc&label=you+are+visitor" alt="visitor count">

<sub>

`brew tap dappermint/tap` &nbsp;·&nbsp; [dappy.lgbt](https://dappy.lgbt) &nbsp;·&nbsp; est. 2025

</sub>

</div>
