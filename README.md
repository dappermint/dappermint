## millia ampora

platform engineer. i build the boring reliable layer under other people's services, and small
sharp tools for myself when the existing ones give up.

most of what i do professionally is private, so this page is the part you can read: macos
internals, terminal tooling, and a wine runtime that should not work but does.

**open to work** &nbsp;·&nbsp; [dappy.lgbt](https://dappy.lgbt)

---

### the day job

kubernetes clusters and the pipelines that feed them. eks, helm, karpenter, the load balancer
controller, k9s when something is on fire. infrastructure in opentofu and ansible, secrets in
vault and sops, aws underneath.

the parts i actually care about: making deploys uneventful, making the failure mode legible
before someone has to guess, and deleting the runbook step that a machine should have been
doing. none of it is public, which is the nature of the work, so take the repos below as
evidence of how i think instead.

---

### things i built

**[ratatouille](https://github.com/dappermint/ratatouille)** &nbsp;· go

macos says "system data: 235 gb" and then refuses to elaborate. `rat` answers the question:
where the space went down to the directory, what is safe to remove with the evidence for each
call written down, and whether the drive itself is healthy. it never removes anything you did
not mark, and it logs everything it does.

**[glass](https://github.com/dappermint/glass)** &nbsp;· go

erlang ships a remote shell, rails ships a console, go ships a debugger. glass is the missing
one: three lines in `main`, then attach to the running service over a unix socket and read or
poke live objects while it takes traffic.

**[winecx-gptk](https://github.com/dappermint/winecx-gptk)** &nbsp;· c, ci

apple's game porting toolkit only executes on crossover-derived wine builds, because d3dmetal
patches their unixcall internals at load time. so i rebased crossover 26.3's wine diff onto
upstream wine 11.15 via a synthetic three-way merge and put the whole thing in ci. steam's ui
end to end, d3d12 through d3dmetal at feature level 12_2, dxvk, msync. the llvm-mingw bug that
stalled steam's login took a module bisection to find.

**[wlipurk-appkit](https://github.com/dappermint/wlipurk-appkit)** &nbsp;· nix

a fap only runs if it was built against the exact firmware sdk it loads on, and the official
catalog will not serve our custom flipper fork. this pins fbt's toolchain in a nix flake and
builds catalog apps from source against our own sdk, no network reach at build time.

**[samsung-ac-remote-flipper-app](https://github.com/dappermint/samsung-ac-remote-flipper-app)** &nbsp;· c

samsung a/c has no one-shot ir codes, only full state frames with a dual-section checksum. so
every button press retransmits the whole state. a flipper zero fap, because my remote broke.

---

### stack

**languages** &nbsp; go · swift · c · nix · python

**platform** &nbsp; kubernetes · eks · helm · k9s · opentofu · ansible · vault · sops · aws

**day to day** &nbsp; macos on nix-darwin · fish · a flipper zero that has ruined several
evenings

---

### elsewhere

[dappy.lgbt](https://dappy.lgbt) &nbsp;·&nbsp; `brew tap dappermint/tap`
